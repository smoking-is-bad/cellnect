# main.py
import os
from fastapi import FastAPI
from fastapi_csrf_protect import CsrfProtect
from pydantic import BaseModel

# CSRF settings from environment variables
class CsrfSettings(BaseModel):
    secret_key: str = os.getenv("CSRF_SECRET_KEY", "default-secret-key")

app = FastAPI()

# Load CSRF configuration
@CsrfProtect.load_config
def get_csrf_config():
    return CsrfSettings()

@app.get("/")
def read_root():
    return {"message": "Hello World"}
