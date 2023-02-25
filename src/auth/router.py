from auth.base_config import fastapi_users
from auth.schemas import UserRead, UserCreate, UserUpdate, EmailBase
from auth.base_config import auth_backend
from fastapi import APIRouter, Depends

from auth.utils import send_email_with_verify_code, create_otp_for_verify
from database import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert
from auth.dependencies import current_user
from auth.models import User, VerifyUser


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


@router.post("/custon_request_verify_token")
async def create_custom_verify_token(user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    secret_code = await create_otp_for_verify()
    verify_dict = {}
    verify_dict["user_id"] = user.id
    verify_dict["code"] = secret_code
    stmt = insert(VerifyUser).values(**verify_dict)
    await session.execute(stmt)
    await session.commit()
    await send_email_with_verify_code(secret_code, [user.email])
    return {'status': 'success'}


@router.post("/custom_verify/")
async def custom_verify_user(secret_key: str):
    pass
