from fastapi import APIRouter

from api.endpoints import router_user

api_router = APIRouter()
api_router.include_router(router_user.router_user, tags=["user"])