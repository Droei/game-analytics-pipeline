from fastapi import FastAPI
from app.routers.test import test_router 

app = FastAPI()

app = FastAPI(
    title="Game Analytics Pipeline",
    version="1.0.0"
)

app.include_router(test_router, prefix="/test", tags=["Test"])

@app.get("/")
def root():
    return {"status": "OK", "message": "Ingestion API running"}

@app.get("/test")
def root():
    return {"status": "OK", "message": "Peeeeeeeeeeeeep"}
