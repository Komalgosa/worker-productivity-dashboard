# AI-Powered Worker Productivity Dashboard

## Overview
This project is a production-style full-stack web application that ingests AI-generated events from factory CCTV systems, computes productivity metrics, and displays them in a dashboard.  
The system is designed to simulate a real-world ML Ops + Analytics pipeline without building any ML models.

---

## Architecture Overview

**Edge → Backend → Dashboard**

1. **Edge (AI Cameras)**
   - AI-powered CCTV cameras generate structured JSON events such as `working`, `idle`, `absent`, and `product_count`.

2. **Backend (FastAPI)**
   - Receives events via REST APIs
   - Validates and stores events
   - Computes productivity metrics

3. **Database (SQLite)**
   - Stores workers, workstations, and events
   - Pre-populated with dummy data for first run

4. **Dashboard (Streamlit)**
   - Displays factory-level, worker-level, and workstation-level metrics
   - Allows filtering and inspection of data

---

## Database Schema

### Workers
| Field | Type |
|-----|------|
| worker_id | String (PK) |
| name | String |

### Workstations
| Field | Type |
|-----|------|
| station_id | String (PK) |
| name | String |

### Events
| Field | Type |
|-----|------|
| timestamp | DateTime |
| worker_id | String (FK) |
| workstation_id | String (FK) |
| event_type | String |
| confidence | Float |
| count | Integer |

---

## Metric Definitions

### Worker-Level Metrics
- **Total Active Time**  
  Sum of time intervals between consecutive `working` events
- **Total Idle Time**  
  Sum of time intervals between consecutive `idle` events
- **Utilization Percentage**  
  `(Active Time / Total Observed Time) × 100`
- **Total Units Produced**  
  Sum of `count` where `event_type = product_count`
- **Units per Hour**  
  `Total Units Produced / Active Time (hours)`

---

### Workstation-Level Metrics
- **Occupancy Time**  
  Total time workers are assigned to a workstation
- **Utilization Percentage**  
  `(Occupancy Time / Available Time) × 100`
- **Total Units Produced**  
  Sum of production events at the workstation
- **Throughput Rate**  
  `Units Produced / Occupancy Time`

---

### Factory-Level Metrics
- **Total Productive Time**  
  Sum of all workers’ active time
- **Total Production Count**  
  Sum of all `product_count` events
- **Average Production Rate**  
  `Total Production / Total Productive Time`
- **Average Utilization**  
  Mean utilization across all workers

---

## Assumptions & Tradeoffs

- Events are sorted by timestamp before processing
- Time difference between events belongs to the previous event
- Events with confidence < 0.5 are ignored
- Missing events are treated as idle time
- SQLite is used for simplicity and quick setup (tradeoff vs scalability)

---

## Handling System Challenges

### Intermittent Connectivity
- Events can be retried by the edge system
- Backend APIs are designed to be idempotent

### Duplicate Events
- Deduplicated using `(timestamp, worker_id, event_type)`

### Out-of-Order Timestamps
- Events are sorted by timestamp before metric computation

---

## Model Lifecycle Considerations (Theoretical)

### Model Versioning
- Each event can include a `model_version`
- A metadata table can track active and historical models

### Model Drift Detection
- Monitor confidence scores and prediction distributions
- Detect deviation from historical baselines

### Retraining Triggers
- Scheduled retraining
- Drift-based retraining
- Performance threshold breaches

---

## Scaling Strategy

### From 5 to 100+ Cameras
- Introduce message queues (Kafka / RabbitMQ)
- Horizontally scale backend services
- Use distributed databases

### Multi-Site Scaling
- Site-wise data partitioning
- Centralized monitoring dashboard
- Cloud object storage for event logs

---

## Running the Project Locally

### Backend
```bash
pip install -r requirements.txt
python backend/init_db.py
uvicorn backend.main:app --reload
