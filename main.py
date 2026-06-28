from fastapi import FastAPI
from app.api import router

app = FastAPI(
    title="InsightFlow AI",
    version="0.1.0",
    description="InsightFlow AI production-grade backend.",
)

app.include_router(router)
