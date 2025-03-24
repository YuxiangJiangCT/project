# Boston Bioprocess Data Visualization Tool
This application allows users to upload fermentation run CSV data files, select parameter options for Pump1 and Pump2, and visualize the data as time series charts.

## Features
- Upload CSV format fermentation run data files
- Select parameters for Pump1 (Glucose or Glycerol)
- Select parameters for Pump2 (Base or Acid)
- Store data in a SQLite database
- Visualize time series data with interactive charts
- View historically uploaded run data

## Technology Stack
- Backend: Python + FastAPI
- Frontend: React + TailwindCSS
- Database: SQLite
- Visualization: Plotly.js
- Containerization: Docker

## Project Link
- [Boston Bioprocess Data Visualization Page](http://3.14.66.6:3000/)
- [Swagger UI](http://3.14.66.6:8000/docs)



## Running the Application

### Using Docker
Using Docker is the simplest way to run the application as it automatically sets up all necessary environments and dependencies.
#### Prerequisites
- [Docker](https://docs.docker.com/get-started/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
#### Getting Started
1. Clone the repository to your local machine:
```bash
git clone https://github.com/YuxiangJiangCT/yxj_bbp.git
cd yxj_bbp
```

2. Build and start the application using Docker Compose:
```bash
docker-compose up --build
```

3. Open your browser and navigate to:
(http://localhost)
   
The application should now be accessible in your browser.

### Without Docker (Development Mode)
If you want to run the application in your local development environment, follow these steps.
#### Prerequisites
Prerequisites
Python 3.9+
Node.js 16+
npm 7+
#### Backend Setup
1. Navigate to the backend directory:
```bash
cd backend
```

2. Create and activate a virtual environment (optional but recommended):
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the backend server:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The backend API should now be running at http://localhost:8000.
#### Frontend Setup
1. In a new terminal window, navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Run the development server:
```bash
npm start
```
The frontend application should now be running at http://localhost:3000.

## Using the Application
### Upload Data File:
- In the left panel, click the "Choose File" button to select a CSV file
- Select a Pump1 parameter (Glucose or Glycerol) from the dropdown menu
- Select a Pump2 parameter (Base or Acid) from the dropdown menu
- Click the "Upload" button
### View Data Visualization:
- After successful upload, the right panel will display the data visualization chart
- The chart shows all parameters (pH, Temperature, and your selected Pump1 and Pump2 parameters) over time
### View Historical Data:
- Use the "Select Run" dropdown menu in the left panel to choose previously uploaded data

## API Documentation
When the backend server is running, you can view the API documentation by visiting:
http://localhost:8000/docs

## Database
The application uses a SQLite database to store data, located at bbp.db in the backend directory. The database contains two tables:
- run_client: Stores run IDs and client names
- run_time_series_data: Stores time series data including timestamps, parameters, values, and units

## Troubleshooting
### Common Issues
1. Cannot connect to backend:
- Ensure the backend server is running
- Check if port 8000 is being used by another application
- Check for CORS errors in the browser console
2. File upload fails:
- Ensure the file format is correct
- Check if the file size is too large
- Look for error messages in the backend logs
3. Docker issues:
- Ensure Docker and Docker Compose are properly installed
- Check if ports 80 and 8000 are in use
- View Docker logs: docker-compose logs

