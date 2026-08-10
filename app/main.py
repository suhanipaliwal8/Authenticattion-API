from fastapi import FastAPI
from sqlalchemy import text

from app.db.database import AsyncSessionLocal
from app.routes.auth import router as auth_router


app = FastAPI(
    title="Authentication API",
    description="A simple authentication API using FastAPI and JWT.",
    version="1.0.0",
)


app.include_router(auth_router)


@app.get("/")
async def root():
    return {"message": "Authentication API is running"}


@app.get("/health")
async def health():
    async with AsyncSessionLocal() as session:
        await session.execute(text("SELECT 1"))

    return {"status": "healthy"}