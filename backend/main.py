from fastapi import FastAPI

from app.api.detections import (
    router as detection_router
)

from app.db.postgres import engine, Base
from app.models.sql.user import User

from app.db.mongo import init_mongodb

from app.api.auth import router as auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sentinel API")


@app.on_event("startup")
async def start_database():
    await init_mongodb()


app.include_router(
    auth_router,
    prefix="/auth",
    tags=["Authentication"]
)

app.include_router(
    detection_router,
    prefix="/detections",
    tags=["Detections"]
)


@app.get("/")
def root():
    return {"message": "Sentinel backend running"}