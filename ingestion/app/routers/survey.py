from fastapi import APIRouter
from pydantic import BaseModel
from utils.db import get_client

router = APIRouter(prefix="/survey", tags=["survey"])

class SurveyResponse(BaseModel):
    player_id: str
    answers: dict
    submitted_at: int

@router.post("/")
def ingest_survey(data: SurveyResponse):
    client = get_client()

    client.command("""
        CREATE TABLE IF NOT EXISTS survey_responses (
            player_id String,
            answers JSON,
            submitted_at UInt64
        ) ENGINE = MergeTree()
        ORDER BY (player_id, submitted_at)
    """)

    client.insert(
        "survey_responses",
        [{
            "player_id": data.player_id,
            "answers": data.answers,
            "submitted_at": data.submitted_at
        }],
        column_names=["player_id", "answers", "submitted_at"]
    )

    return {"status": "ok", "inserted": data}
