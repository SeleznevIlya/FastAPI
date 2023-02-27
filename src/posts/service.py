from sqlalchemy import select, insert
from posts.models import Post


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
