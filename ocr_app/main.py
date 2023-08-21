import uvicorn
from fastapi import FastAPI

from ocr_app.api.v1.api import router as api_router

app = FastAPI()
app.include_router(api_router)


if __name__ == "__main__":
    uvicorn.run("ioc_project.main:app", host="0.0.0.0", port=8000, reload=True)
