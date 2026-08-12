from fastapi import APIRouter

from app.routes.endpoints import Users

router = APIRouter()

router.include_router(Users.router) 