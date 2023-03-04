from fastapi import FastAPI
from auth.router import router as auth_router
from posts.router import router as post_router
from redis import asyncio as aioredis

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
import time

app = FastAPI(
    title='My FastAPI App'
)

app.include_router(auth_router)
app.include_router(post_router)


@app.on_event("startup")
async def startup_event():
    redis = aioredis.from_url("redis://localhost", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
