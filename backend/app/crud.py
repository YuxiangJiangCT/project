from sqlalchemy.orm import Session
from .models import RunClient, RunTimeSeriesData

def get_run_client(db: Session, run_id: str):
    return db.query(RunClient).filter(RunClient.run_id == run_id).first()

def create_run_client(db: Session, run_id: str, client_name: str):
    db_client = RunClient(run_id=run_id, client_name=client_name)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

def get_time_series_data(db: Session, run_id: str):
    return db.query(RunTimeSeriesData).filter(RunTimeSeriesData.run_id == run_id).all()

def create_time_series_data(db: Session, data_dict):
    db_data = RunTimeSeriesData(**data_dict)
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data

def get_all_runs(db: Session):
    return db.query(RunClient).all()

def get_parameters_for_run(db: Session, run_id: str):
    """Get unique parameters for a specific run"""
    results = db.query(RunTimeSeriesData.parameter).filter(
        RunTimeSeriesData.run_id == run_id
    ).distinct().all()
    return [r[0] for r in results]
