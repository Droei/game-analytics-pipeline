from typing import Any, Dict
from pydantic import BaseModel, Field

class PlayerEvent(BaseModel):
    player_id: str
    event: str
    timestamp: str
    metadata: Dict[str, Any] = Field(default_factory=dict)
    session_id: str | None = None
    platform: str | None = None
    build_version: str | None = None