from fastapi import APIRouter, File, UploadFile
from fastapi.responses import JSONResponse
import pytesseract
from PIL import Image
import numpy as np
import cv2
import io
from ocr_app.parsing import credit_card, hash, parse

router = APIRouter(
    prefix="/api/v1/ocr",
    tags=["ocr"],
    responses={404: {"description": "Not found"}},
)


@router.post("/file")
async def read_user(file: UploadFile = File(...)):
    try:

        img = Image.open(io.BytesIO(file.file.read()))

        image_np = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

        gray_img = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)

        pytesseract_result = pytesseract.image_to_string(gray_img)

        result: list = await parse.parse_text(pytesseract_result)

        if pytesseract_result is None:
            return JSONResponse(content={"content": None}, status_code=204)

        return JSONResponse(
            content={"content": pytesseract_result, "findings": result}, status_code=200
        )

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
