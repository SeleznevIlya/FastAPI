from auth.base_config import fastapi_users
from auth.schemas import UserRead, UserCreate, UserUpdate, EmailBase
from auth.base_config import auth_backend
from fastapi import APIRouter, Depends
from database import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from auth.dependencies import current_user
from auth.models import User
from auth.service import verify_user, create_verification_token

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

router.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)

router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)


@router.post("/custom_request_verification_token")
async def create_custom_verification_token(user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    return await create_verification_token(user, session)


@router.post("/custom_verify/")
async def custom_verify_user(secret_key: str, user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    return await verify_user(secret_key, user, session)
