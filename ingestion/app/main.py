from fastapi import FastAPI

app = FastAPI(title="Game Analytics Pipeline")

@app.get("/health")
def health_check():
    return {"status": "ok"}
