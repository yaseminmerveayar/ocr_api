from fastapi import APIRouter
from ocr_app.api.v1.endpoints import ocr

router = APIRouter()
router.include_router(ocr.router)
