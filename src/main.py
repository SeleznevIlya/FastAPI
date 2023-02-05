from fastapi import FastAPI
from operations.schemas import Trade
from typing import List

from auth.base_config import fastapi_users
from auth.schemas import UserRead, UserCreate
from auth.base_config import auth_backend


app = FastAPI(
    title='My FastAPI App'
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

