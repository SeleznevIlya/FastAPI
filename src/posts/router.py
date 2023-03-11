from fastapi import APIRouter, Depends
from database import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from posts.schemas import PostCreate, PostList, PostBase, CommentBase, CommentCreate, CommentList
from auth.dependencies import current_user
from auth.models import User
from typing import List
from posts.service import (_get_post,
						   _get_posts,
						   _create_post,
						   create_comment_from_current_user,
						   get_comments_selected_post_,
						   get_comment_selected_user_,
						   dislike_post,
						   like_post,
						   like_comment,
						   dislike_comment)


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


@router.get('/comment/{user_id}', response_model=List[CommentList])
async def get_comments_selected_user(user_id: int, session: AsyncSession = Depends(get_async_session)):
	return await get_comment_selected_user_(user_id, session)


@router.post('/comment/')
async def create_comment(new_comment: CommentCreate, post_id: int, user: User = Depends(current_user),
					  session: AsyncSession = Depends(get_async_session)):
	return await create_comment_from_current_user(new_comment, post_id, user, session)


@router.get('/comment/{post_id}/', response_model=List[CommentList])
async def get_comments_selected_post(post_id: int, session: AsyncSession = Depends(get_async_session)):
	return await get_comments_selected_post_(post_id, session)


@router.post('/like/')
async def add_like_post(db_object_id: int, session: AsyncSession = Depends(get_async_session)):
	return await like_post(db_object_id, session)


@router.post('/dislike/')
async def add_dislike_post(db_object_id: int, session: AsyncSession = Depends(get_async_session)):
	return await dislike_post(db_object_id, session)


@router.post('/comment/like/')
async def add_like_comment(db_object_id: int, session: AsyncSession = Depends(get_async_session)):
	return await like_comment(db_object_id, session)


@router.post('/comment/dislike/')
async def add_dislike_comment(db_object_id: int, session: AsyncSession = Depends(get_async_session)):
	return await dislike_comment(db_object_id, session)
