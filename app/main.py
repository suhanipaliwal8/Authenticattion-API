from fastapi import FastAPI
from sqlalchemy import text

from app.config import settings
from app.db.database import AsyncSessionLocal


app = FastAPI(
    title="Authentication API",
    description="A simple authentication API using FastAPI and JWT.",
    version="1.0.0",
)


@app.get("/")
async def root():
    return {"message": "Authentication API is running"}


@app.get("/health")
async def health():
    async with AsyncSessionLocal() as session:
        await session.execute(text("SELECT 1"))

    return {"status": "healthy"}


@app.get("/config-test")
async def config_test():
    return {
        "algorithm": settings.JWT_ALGORITHM,
        "token_expiration": settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES,
    }