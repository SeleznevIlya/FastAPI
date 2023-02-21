from fastapi import APIRouter, Depends
from database import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert
from posts.models import Post
from posts.schemas import PostCreate
from auth.dependencies import current_user
from auth.models import User

router = APIRouter(
	prefix="/posts",
	tags=["Posts"]
)


@router.get('/')
async def get_posts(session: AsyncSession = Depends(get_async_session)):
	query = select(Post)
	result = await session.execute(query)
	return result.all()


@router.get('/{id}')
async def get_post(id: int, session: AsyncSession = Depends(get_async_session)):
	query = select(Post).where(Post.id == id)
	result = await session.execute(query)
	return result


@router.post('/')
async def create_post(new_post: PostCreate, user: User = Depends(current_user),
					session: AsyncSession = Depends(get_async_session)):
	queue = insert(Post).values(Post.user_id == user.id, **new_post.dict())
	await session.execute(queue)
	await session.commit()
	return {'status': 'success'}
