from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os
from .database import SessionLocal, init_db
from .models import RunClient, RunTimeSeriesData
from .utils import parse_csv

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_db()

@app.post("/upload/")
async def upload_file(
    file: UploadFile = File(...),
    pump1_choice: str = Form(...),
    pump2_choice: str = Form(...)
):
    file_location = f"temp_{file.filename}"
    with open(file_location, "wb") as f:
        shutil.copyfileobj(file.file, f)

    try:
        client_name, run_id, records = parse_csv(file_location, file.filename, pump1_choice, pump2_choice)
        if not client_name or not run_id:
            raise HTTPException(status_code=400, detail="Could not parse client info and run ID from file")
        
        db = SessionLocal()
        try:
            existing = db.query(RunClient).filter(RunClient.run_id == run_id).first()
            if not existing:
                client_entry = RunClient(run_id=run_id, client_name=client_name)
                db.add(client_entry)
                db.commit()
            
            for rec in records:
                entry = RunTimeSeriesData(
                    run_id=rec["run_id"],
                    time_stamp=rec["time_stamp"],
                    parameter=rec["parameter"],
                    process_value=rec["process_value"],
                    units=rec["units"]
                )
                db.add(entry)
            db.commit()
            
            return {"message": "File uploaded and parsed successfully", "run_id": run_id, "client_name": client_name}
        finally:
            db.close()
    finally:
        if os.path.exists(file_location):
            os.remove(file_location)

@app.get("/data/{run_id}")
def get_data(run_id: str):
    db = SessionLocal()
    try:
        client = db.query(RunClient).filter(RunClient.run_id == run_id).first()
        if not client:
            raise HTTPException(status_code=404, detail=f"Run ID {run_id} not found")
        
        results = db.query(RunTimeSeriesData).filter(RunTimeSeriesData.run_id == run_id).all()
        
        data = []
        for result in results:
            data.append({
                "id": result.id,
                "run_id": result.run_id,
                "time_stamp": result.time_stamp,
                "parameter": result.parameter,
                "process_value": result.process_value,
                "units": result.units
            })
        
        return {
            "client_name": client.client_name,
            "run_id": run_id,
            "data": data
        }
    finally:
        db.close()

@app.get("/runs")
def get_runs():
    db = SessionLocal()
    try:
        runs = db.query(RunClient).all()
        return [{"run_id": run.run_id, "client_name": run.client_name} for run in runs]
    finally:
        db.close()