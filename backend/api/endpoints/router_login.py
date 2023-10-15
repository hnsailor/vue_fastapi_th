from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
import jwt
from datetime import datetime, timedelta

from models.models_users import User
from utils import verify_password, create_jwt_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
router_login = APIRouter()


@router_login.post("/token")
def login(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user:
        raise HTTPException(status_code=400, detail="用户名不存在")
    if not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="密码错误")
    data = {
        "username": user.username,
        "password": user.hashed_password
    }
    token = create_jwt_token(data)
    return {"access_token": token, "token_type": "bearer"}
