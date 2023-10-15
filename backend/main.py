from fastapi import FastAPI

app = FastAPI(
    title="查寝",
    description="查寝系统",
)


def init_db():
    from db.database import Base, engine
    from models.models_users import User
    Base.metadata.create_all(bind=engine)


init_db()
