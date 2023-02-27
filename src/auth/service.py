from sqlalchemy import select, insert
from auth.models import VerifyUser
from auth.utils import (delete_code_from_db,
						update_users_verified_status,
						send_email_with_verify_code,
						create_otp_for_verify)


async def create_verification_token(user, session):
	if not user.is_verified:
		await delete_code_from_db(user, session)
		secret_code = await create_otp_for_verify()
		verify_dict = dict()
		verify_dict["user_id"] = user.id
		verify_dict["code"] = secret_code
		stmt = insert(VerifyUser).values(**verify_dict)
		await session.execute(stmt)
		await session.commit()
		await send_email_with_verify_code(secret_code, [user.email])
		return {
			"status": "success",
			"data": None,
			"details": "Secret code sent to email"
		}
	else:
		return {
			"status": "error",
			"data": None,
			"details": "User already verified"
		}


async def verify_user(secret_key, user, session):
	if not user.is_verified:
		query = select(VerifyUser.code).where(VerifyUser.user_id == user.id)
		secret_key_from_db = await session.execute(query)
		if secret_key == secret_key_from_db.first()[0]:
			await update_users_verified_status(user, session)
			await delete_code_from_db(user, session)
		return {
			"status": "success",
			"data": None,
			"details": "Verification is success"
		}
	else:
		return {
			"status": "error",
			"data": None,
			"details": "User already verified"
		}
