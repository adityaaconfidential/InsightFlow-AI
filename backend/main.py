from fastapi import FastAPI
from app.api import router

app = FastAPI(
    title="InsightFlow API",
    version="0.1.0",
    description="Backend API for InsightFlow-AI",
)

app.include_router(router)
