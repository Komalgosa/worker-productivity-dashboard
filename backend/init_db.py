from database import engine, SessionLocal
from models import Base, Worker, Workstation

Base.metadata.create_all(bind=engine)

db = SessionLocal()

# Seed workers
workers = [
    Worker(worker_id="W1", name="Amit"),
    Worker(worker_id="W2", name="Ravi"),
    Worker(worker_id="W3", name="Neha"),
    Worker(worker_id="W4", name="Sita"),
    Worker(worker_id="W5", name="John"),
    Worker(worker_id="W6", name="Priya"),
]

# Seed workstations
stations = [
    Workstation(station_id="S1", name="Assembly"),
    Workstation(station_id="S2", name="Packing"),
    Workstation(station_id="S3", name="Welding"),
    Workstation(station_id="S4", name="Painting"),
    Workstation(station_id="S5", name="Testing"),
    Workstation(station_id="S6", name="QC"),
]

db.add_all(workers + stations)
db.commit()
db.close()

print("Database initialized with dummy data")
