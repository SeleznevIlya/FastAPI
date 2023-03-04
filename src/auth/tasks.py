from celery import Celery
from pydantic import EmailStr
from typing import List
from fastapi_mail import FastMail, MessageSchema, MessageType
from config import conf
from starlette.responses import JSONResponse
import time


celery = Celery('tasks', broker='redis://localhost:6379')


@celery.task
def send_email_after_registration(email: List[EmailStr]) -> JSONResponse:
    html = """<p>Thank you for registering</p> """

    message = MessageSchema(
        subject="Fastapi-Mail module",
        recipients=email,
        body=html,
        subtype=MessageType.html)
    fm = FastMail(conf)
    fm.send_message(message)
    return JSONResponse(status_code=200, content={"message": "email has been sent"})
