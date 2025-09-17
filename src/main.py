from fastapi import FastAPI
from pydantic import BaseModel
import datetime

app = FastAPI(
    title="Analytics Service API",
    description="Tracks and analyzes events and metrics across the platform",
    version="1.0.0"
)

class Event(BaseModel):
    event_type: str
    user_id: int
    metadata: dict

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "analytics-service"}

@app.post("/events")
def track_event(event: Event):
    # TODO: Stream to Kafka and insert into InfluxDB/Postgres
    return {
        "message": "event received",
        "event_type": event.event_type,
        "timestamp": datetime.datetime.utcnow().isoformat()
    }

@app.get("/metrics/{metric_name}")
def get_metric(metric_name: str):
    # Mocked response for now
    return {
        "metric": metric_name,
        "value": 42,
        "timestamp": datetime.datetime.utcnow().isoformat()
    }
