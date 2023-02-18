from auth.base_config import fastapi_users
from auth.schemas import UserRead, UserCreate
from auth.base_config import auth_backend
from fastapi import APIRouter

router = APIRouter()


router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)