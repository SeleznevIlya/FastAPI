from fastapi import FastAPI
from posts.schemas import Trade
from typing import List

from auth.router import router as auth_router

app = FastAPI(
    title='My FastAPI App'
)

app.include_router(auth_router)
