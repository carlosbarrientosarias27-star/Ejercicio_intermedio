from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="To-Do API")

app.include_router(router)