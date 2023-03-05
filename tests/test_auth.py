import pytest
from sqlalchemy import insert, select

from auth.models import Role
from conftest import client, async_session_maker


async def test_add_role():
	async with async_session_maker() as session:
		stmt = insert(Role).values(id=1, name="admin", permissions=None)
		await session.execute(stmt)
		await session.commit()

		query = select(Role)
		result = await session.execute(query)
		assert result.all()[0][0].id == 1, "Роль не добавилась"


def test_register():
	response = client.post("/auth/register", json={
		"email": "user@example.com",
		"password": "string",
		"is_active": True,
		"is_superuser": False,
		"is_verified": False,
		"username": "string",
		"role_id": 1
	})

	assert response.status_code == 201
