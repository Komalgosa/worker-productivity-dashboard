# AI-Powered Worker Productivity Dashboard

## Architecture
CCTV → Backend (FastAPI) → Database (SQLite) → Dashboard (Streamlit)

## Database Schema
- Workers(worker_id, name)
- Workstations(station_id, name)
- Events(timestamp, worker_id, station_id, event_type, count)

## Metrics
- Active time = working events
- Idle time = idle events
- Units = sum(product_count)

## Assumptions
- Events are sequential
- Missing events are ignored
- Confidence < 0.5 ignored

## Handling Issues
- Duplicate events: dedup by timestamp + worker_id
- Out-of-order: sorted by timestamp
- Connectivity: retry on failure

## Scaling
- Kafka for ingestion
- PostgreSQL
- Microservices per factory
