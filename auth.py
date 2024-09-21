# auth.py
from fastapi import APIRouter, Depends, HTTPException, Request, Form
from fastapi_csrf_protect import CsrfProtect
from sqlalchemy.orm import Session
from .crud import get_user_by_username
from starlette.responses import JSONResponse
from .database import get_db

auth_router = APIRouter()

@auth_router.post("/auth/login")
def login(username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db), csrf_protect: CsrfProtect = Depends()):
    # Check CSRF token for POST requests
    csrf_protect.validate_csrf_in_cookies()
    
    user = get_user_by_username(db, username)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    # If login is successful, set CSRF token in response cookie
    response = JSONResponse({"message": "Login successful"})
    csrf_token = csrf_protect.generate_csrf()
    response.set_cookie(key="csrf_token", value=csrf_token)
    return response
