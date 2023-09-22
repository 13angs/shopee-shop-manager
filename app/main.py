from fastapi import FastAPI
from app.api.routers import comment

app = FastAPI()

app.include_router(comment.router)
