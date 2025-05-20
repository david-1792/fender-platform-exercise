from fastapi import APIRouter

from app.api.login.router import router as login_router
from app.api.users.router import router as users_router

router = APIRouter()

router.include_router(login_router)
router.include_router(users_router)