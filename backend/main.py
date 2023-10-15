from fastapi import FastAPI

from api.endpoints import router_user

app = FastAPI(
    title="查寝",
    description="查寝系统",
)

app.include_router(router_user.router_user, tags=["user"])


def init_db():
    from db.database import Base, engine
    from models.models_users import User
    Base.metadata.create_all(bind=engine)


init_db()
