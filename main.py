# main.py
from fastapi import FastAPI, Depends
from fastapi_csrf_protect import CsrfProtect
from pydantic import BaseModel
from .auth import auth_router
from .database import Base, engine

Base.metadata.create_all(bind=engine)

class CsrfSettings(BaseModel):
    secret_key: str = "your-csrf-secret-key"  # Ensure this is a secure key

app = FastAPI()

# Initialize CSRF protection
@CsrfProtect.load_config
def get_csrf_config():
    return CsrfSettings()

app.include_router(auth_router)
