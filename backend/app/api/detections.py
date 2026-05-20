from fastapi import APIRouter, Depends

from app.auth.dependencies import get_current_user

from app.schemas.detection_schema import (
    DetectionUpload
)

from app.models.mongo.detection_event import (
    DetectionEvent,
    Detection
)

router = APIRouter()


@router.post("/upload")
async def upload_detection(
    payload: DetectionUpload,
    current_user: str = Depends(get_current_user)
):

    detection_objects = [
        Detection(
            label=d.label,
            confidence=d.confidence,
            bbox=d.bbox
        )
        for d in payload.detections
    ]

    event = DetectionEvent(
        device_id=payload.device_id,
        user_id=current_user,
        detections=detection_objects
    )

    await event.insert()

    return {
        "message": "Detection uploaded successfully"
    }

@router.get("/history")
async def get_detection_history(
    current_user: str = Depends(get_current_user)
):

    events = await DetectionEvent.find(
        DetectionEvent.user_id == current_user
    ).to_list()

    return events