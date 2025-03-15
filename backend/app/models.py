from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Float  


Base = declarative_base()

class RunClient(Base):
    __tablename__ = "run_client"
    id = Column(Integer, primary_key=True, index=True)
    run_id = Column(String, unique=True, index=True, nullable=False)
    client_name = Column(String, nullable=False)

class RunTimeSeriesData(Base):
    __tablename__ = "run_time_series_data"
    id = Column(Integer, primary_key=True, index=True)
    run_id = Column(String, ForeignKey("run_client.run_id"), nullable=False)
    time_stamp = Column(Float, nullable=False)  
    parameter = Column(String, nullable=False)
    process_value = Column(Float, nullable=False)
    units = Column(String, nullable=False)