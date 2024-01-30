from app.api.test_api import router as test_router
from fastapi import FastAPI

app = FastAPI()

app.include_router(test_router)
