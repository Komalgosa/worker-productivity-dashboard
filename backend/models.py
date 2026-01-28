from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey
from database import Base
from datetime import datetime

class Worker(Base):
    __tablename__ = "workers"

    worker_id = Column(String, primary_key=True, index=True)
    name = Column(String)

class Workstation(Base):
    __tablename__ = "workstations"

    station_id = Column(String, primary_key=True, index=True)
    name = Column(String)

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    worker_id = Column(String, ForeignKey("workers.worker_id"))
    workstation_id = Column(String, ForeignKey("workstations.station_id"))
    event_type = Column(String)   # working, idle, absent, product_count
    confidence = Column(Float)
    count = Column(Integer, default=0)
