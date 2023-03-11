from sqlalchemy import select, insert, update
from posts.models import Post, Comment


async def _get_posts(session):
	query = select(Post)
	result = await session.execute(query)
	return result.scalars().all()


async def _get_post(post_id, session):
	query = select(Post).where(Post.id == post_id)
	result = await session.execute(query)
	return result.scalars().all()


async def _create_post(new_post, user, session):
	post_values = new_post.dict()
	post_values['user_id'] = user.id
	stmt = insert(Post).values(**post_values)
	await session.execute(stmt)
	await session.commit()
	return {'status': 'success'}


async def create_comment_from_current_user(new_comment, post_id, user, session):
	comment = new_comment.dict()
	comment['author_id'] = user.id
	comment['post_id'] = post_id
	stmt = insert(Comment).values(**comment)
	await session.execute(stmt)
	await session.commit()
	return {'status': 'Comment creation succesfuly'}


async def get_comments_selected_post_(post_id, session):
	query = select(Comment).where(Comment.post_id == post_id)
	result = await session.execute(query)
	return result.scalars().all()


async def get_comment_selected_user_(user_id, session):
	query = select(Comment).where(Comment.author_id == user_id)
	result = await session.execute(query)
	return result.scalars().all()


async def like_post(db_object_id, session):
	return await like(Post, db_object_id, session)


async def dislike_post(db_object_id, session):
	return await dislike(Post, db_object_id, session)


async def like_comment(db_object_id, session):
	return await like(Comment, db_object_id, session)


async def dislike_comment(db_object_id, session):
	return await dislike(Comment, db_object_id, session)


async def like(db_object, db_object_id, session):
	query = select(db_object.rating).where(db_object.id == db_object_id)
	rating_from_db = await session.execute(query)
	stmt = update(db_object).where(db_object.id == db_object_id).values({"rating": rating_from_db.first()[0]+1})
	await session.execute(stmt)
	await session.commit()
	return None


async def dislike(db_object, db_object_id, session):
	query = select(db_object.rating).where(db_object.id == db_object_id)
	rating_from_db = await session.execute(query)
	stmt = update(db_object).where(db_object.id == db_object_id).values({"rating": rating_from_db.first()[0] - 1})
	await session.execute(stmt)
	await session.commit()
	return None
