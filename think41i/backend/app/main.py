from fastapi import FastAPI
from .routes import chat
from .database import engine
from .models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(chat.router, prefix="/api")
