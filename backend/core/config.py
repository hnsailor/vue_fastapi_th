import os
import secrets
from typing import List
from datetime import timedelta
from pydantic_settings import BaseSettings

JWT_SECRET = 'secret'
JWT_ALGORITHM = 'HS256'
JWT_EXPIRE_MINUTES = 60 * 24 * 7  # one week

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # one week
    BACKEND_CORS_ORIGINS: List[str] = ["*"]

    SQLALCHEMY_DATABASE_URI: str = f"sqlite:///{os.path.join(BASE_DIR, '../sql_app.db')}"


settings = Settings()
