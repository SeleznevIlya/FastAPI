from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from fastapi import Depends
from starlette.responses import JSONResponse

from auth.models import User
from database import get_async_session
from fastapi_mail import FastMail, MessageSchema, MessageType
from config import conf
from typing import List
from pydantic import EmailStr


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)


async def send_email_after_registration(email: List[EmailStr]) -> JSONResponse:
    html = """<p>Thank you for registering</p> """

    message = MessageSchema(
        subject="Fastapi-Mail module",
        recipients=email,
        body=html,
        subtype=MessageType.html)

    fm = FastMail(conf)
    await fm.send_message(message)
    return JSONResponse(status_code=200, content={"message": "email has been sent"})
