from fastapi import APIRouter, File, UploadFile
from fastapi.responses import JSONResponse
import pytesseract
from PIL import Image
import numpy as np
import cv2
import io
from ocr_app.parsing import parse
import redis
import hashlib
import json

router = APIRouter(
    prefix="/api/v1/ocr",
    tags=["ocr"],
    responses={404: {"description": "Not found"}},
)

redis_client = redis.Redis(host="cache", port=6379, db=0)


@router.post("/file")
async def read_user(file: UploadFile = File(...)):
    if not is_valid_image(file.content_type):
        return JSONResponse(
            content={"status": "bad request. wrong file format."}, status_code=400
        )

    img = Image.open(io.BytesIO(file.file.read()))
    img_bytes = img.tobytes()
    file_hash = hashlib.sha256(img_bytes).hexdigest()

    cache: json = redis_client.get(file_hash)
    if cache:
        cache_data = json.loads(cache.decode("utf-8"))
        return JSONResponse(content=cache_data, status_code=200)

    else:
        pytesseract_result = pytesseract.image_to_string(img)
        cleaned_response: str = (
            pytesseract_result.replace("\n", "")
            .replace("\t", "")
            .replace("\r", "")
            .replace("\f", "")
        )
        if not cleaned_response:
            return JSONResponse(content=None, status_code=204)
        else:
            findings: list = await parse.parse_text(pytesseract_result)
            result = {
                "content": pytesseract_result,
                "status": "successfull",
                "findings": findings,
            }

            json_result = json.dumps(result)
            redis_client.set(file_hash, json_result, ex=1 * 3600)

            return JSONResponse(content=result, status_code=200)


def is_valid_image(content_type):
    valid_image_types = [
        "image/jpeg",
        "image/png",
        "image/gif",
        "image/avif",
        "image/apng",
        "image/svg+xml",
        "image/webp",
    ]
    return content_type in valid_image_types
