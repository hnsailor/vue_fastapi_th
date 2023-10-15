from datetime import timedelta, datetime

import jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from models.models_users import User
from core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def create_jwt_token(data: dict):
    expiration = str(datetime.utcnow()) + str(settings.JWT_EXPIRE_MINUTES)
    to_encode = data.copy()
    to_encode.update({"exp": expiration})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    return encoded_jwt
