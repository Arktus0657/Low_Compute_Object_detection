from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

from app.core.config import settings
from app.models.mongo.detection_event import DetectionEvent


client = AsyncIOMotorClient(settings.MONGODB_URL)


async def init_mongodb():
    database = client.get_database("sentinel_ai")

    await init_beanie(
        database=database,
        document_models=[DetectionEvent]
    )