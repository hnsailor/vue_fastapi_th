from fastapi import APIRouter

from api.endpoints import router_user, router_login

api_router = APIRouter()
api_router.include_router(router_user.router_user, prefix="/user", tags=["user"])
api_router.include_router(router_login.router_login, prefix="/login", tags=["login"])
