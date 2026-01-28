from fastapi import FastAPI
from datetime import datetime
from typing import List

app = FastAPI()

# Dummy data
workers = [
    {"worker_id": "W1", "name": "Amit"},
    {"worker_id": "W2", "name": "Ravi"},
    {"worker_id": "W3", "name": "Neha"},
    {"worker_id": "W4", "name": "Sita"},
    {"worker_id": "W5", "name": "John"},
    {"worker_id": "W6", "name": "Priya"},
]

stations = [
    {"station_id": "S1", "name": "Assembly"},
    {"station_id": "S2", "name": "Packing"},
    {"station_id": "S3", "name": "Welding"},
    {"station_id": "S4", "name": "Painting"},
    {"station_id": "S5", "name": "Testing"},
    {"station_id": "S6", "name": "QC"},
]

events = []

@app.get("/")
def home():
    return {"message": "Backend running"}

@app.post("/ingest-event")
def ingest_event(event: dict):
    events.append(event)
    return {"status": "event stored"}

@app.get("/metrics")
def get_metrics():
    return {
        "total_events": len(events),
        "total_workers": len(workers),
        "total_stations": len(stations)
    }
