from fastapi import FastAPI
from sqlalchemy import text

from app.db.database import AsyncSessionLocal
from app.middleware.auth import AuthMiddleware
from app.routes.auth import router as auth_router

from app.logging_config import setup_logging
from app.middleware.logging import LoggingMiddleware

setup_logging()

app = FastAPI(
    title="Authentication API",
    description="A simple authentication API using FastAPI and JWT.",
    version="1.0.0",
)

app.add_middleware(AuthMiddleware)
app.add_middleware(LoggingMiddleware)


app.include_router(auth_router)


@app.get("/")
async def root():
    return {"message": "Authentication API is running"}


@app.get("/health")
async def health():
    try:
        async with AsyncSessionLocal() as session:
            await session.execute(text("SELECT 1"))

        return {
            "status": "healthy",
            "database": "connected",
        }

    except Exception:
        return {
            "status": "unhealthy",
            "database": "disconnected",
        }