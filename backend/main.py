from fastapi import FastAPI

from api.api import api_router

app = FastAPI(
    title="查寝",
    description="查寝系统",
)

app.include_router(api_router)


def init_db():
    from db.database import Base, engine
    from models.models_users import User
    from models.models_sanitation import Sanitation
    from models.models_class_info import Grade, Major, Classes, Dorm
    Base.metadata.create_all(bind=engine)


init_db()
