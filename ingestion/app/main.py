from fastapi import FastAPI
from routers import events, survey

app = FastAPI(
    title="Game Analytics Pipeline",
    version="1.0.0"
)

app.include_router(events.router)
app.include_router(survey.router)

@app.get("/")
def root():
    return {"status": "OK", "message": "Ingestion API running"}
