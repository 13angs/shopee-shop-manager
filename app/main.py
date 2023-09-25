from fastapi import FastAPI
from app.api.routers import comment, invoice

app = FastAPI()

app.include_router(comment.router)
app.include_router(invoice.router)
