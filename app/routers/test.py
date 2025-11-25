from datetime import datetime
from typing import Any, Dict, List
from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field
from clickhouse_connect import get_client

class PlayerEvent(BaseModel):
    player_id: str
    event: str
    timestamp: datetime
    metadata: Dict[str, Any] = Field(default_factory=dict)
    session_id: str | None = None
    platform: str | None = None
    build_version: str | None = None

test_router = APIRouter()

def get_ch_client():
    client = get_client(host="localhost", username="default", password="meep")
    
    client.command("""
    CREATE TABLE IF NOT EXISTS default.player_events (
        player_id String,
        event String,
        timestamp DateTime64(3, 'UTC'),
        metadata JSON,
        session_id String,
        platform LowCardinality(String),
        build_version String
    )
    ENGINE = MergeTree()
    ORDER BY (player_id, timestamp)
    """)
    
    return client

@test_router.post("/log")
def log_event(event: PlayerEvent, client = Depends(get_ch_client)):
    client.insert(
        "player_events",
        [[
            event.player_id,
            event.event,
            event.timestamp.isoformat(),
            event.metadata,
            event.session_id or "",
            event.platform or "",
            event.build_version or "",
        ]]
    )
    return {"status": "ok"}

@test_router.get("/logs", response_model=List[PlayerEvent])
def get_all_events(client = Depends(get_ch_client)):
    rows = client.query("SELECT * FROM default.player_events ORDER BY timestamp ASC").result_rows
    events = []
    for row in rows:
        events.append(
            PlayerEvent(
                player_id=row[0],
                event=row[1],
                timestamp=row[2],
                metadata=row[3],
                session_id=row[4] if row[4] else None,
                platform=row[5] if row[5] else None,
                build_version=row[6] if row[6] else None
            )
        )
    return events