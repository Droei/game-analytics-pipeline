from fastapi import APIRouter
from pydantic import BaseModel
from utils.db import get_client

router = APIRouter(prefix="/events", tags=["events"])

class GameEvent(BaseModel):
    player_id: str
    event_type: str
    timestamp: int
    metadata: dict | None = None

@router.post("/")
def ingest_event(event: GameEvent):
    client = get_client()

    client.command("""
        CREATE TABLE IF NOT EXISTS game_events (
            player_id String,
            event_type String,
            timestamp UInt64,
            metadata JSON
        ) ENGINE = MergeTree()
        ORDER BY (player_id, timestamp)
    """)

    client.insert(
        "game_events",
        [{
            "player_id": event.player_id,
            "event_type": event.event_type,
            "timestamp": event.timestamp,
            "metadata": event.metadata
        }],
        column_names=["player_id", "event_type", "timestamp", "metadata"]
    )

    return {"status": "ok", "inserted": event}
