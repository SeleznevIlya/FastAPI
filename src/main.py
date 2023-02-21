from fastapi import FastAPI
from typing import List

from auth.router import router as auth_router
from posts.router import router as post_router

app = FastAPI(
    title='My FastAPI App'
)

app.include_router(auth_router)
app.include_router(post_router)
