from beanie import Document
from pydantic import BaseModel

from typing import List


class Detection(BaseModel):
    label: str
    confidence: float
    bbox: List[int]


class DetectionEvent(Document):
    device_id: str
    user_id: str
    detections: List[Detection]

    class Settings:
        name = "detection_events"