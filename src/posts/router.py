from fastapi import APIRouter, Depends
from database import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from posts.schemas import PostCreate, PostList, PostBase
from auth.dependencies import current_user
from auth.models import User
from typing import List
from posts.service import _get_post, _get_posts, _create_post

router = APIRouter(
	prefix="/posts",
	tags=["Posts"]
)


@router.get('/', response_model=List[PostList])
async def get_posts(session: AsyncSession = Depends(get_async_session)):
	return await _get_posts(session)


@router.get('/{post_id}/', response_model=List[PostBase])
async def get_post(post_id: int, session: AsyncSession = Depends(get_async_session)):
	return await _get_post(post_id, session)


@router.post('/')
async def create_post(new_post: PostCreate, user: User = Depends(current_user),
					  session: AsyncSession = Depends(get_async_session)):
	return await _create_post(new_post, user, session)
