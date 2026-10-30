"""FastAPI application. Run with: uvicorn app:app --reload"""

from fastapi import FastAPI

from routers.events import router as event_router

app = FastAPI(title="NC Plus One")
app.include_router(event_router, prefix="/api")