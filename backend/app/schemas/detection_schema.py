from pydantic import BaseModel
from typing import List


class DetectionItem(BaseModel):
    label: str
    confidence: float
    bbox: List[int]


class DetectionUpload(BaseModel):
    device_id: str
    detections: List[DetectionItem] 