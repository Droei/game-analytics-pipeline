from fastapi import APIRouter

test_router = APIRouter()

@test_router.get("/hello")
async def hello():
    return {"message": "Hello from test router!"}