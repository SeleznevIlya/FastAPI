from fastapi import APIRouter, Depends
from database import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert
from posts.models import Post
from posts.schemas import PostCreate, PostList, PostBase
from auth.dependencies import current_user
from auth.models import User
from typing import List

router = APIRouter(
	prefix="/posts",
	tags=["Posts"]
)


@router.get('/', response_model=List[PostList])
async def get_posts(session: AsyncSession = Depends(get_async_session)):
	query = select(Post)
	result = await session.execute(query)
	return result.scalars().all()


@router.get('/{post_id}/', response_model=List[PostBase])
async def get_post(post_id: int, session: AsyncSession = Depends(get_async_session)):
	query = select(Post).where(Post.id == post_id)
	result = await session.execute(query)
	return result.scalars().all()


@router.post('/')
async def create_post(new_post: PostCreate, user: User = Depends(current_user),
					  session: AsyncSession = Depends(get_async_session)):
	post_values = new_post.dict()
	post_values['user_id'] = user.id
	stmt = insert(Post).values(**post_values)
	await session.execute(stmt)
	await session.commit()
	return {'status': 'success'}
