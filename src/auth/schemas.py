from fastapi_users import schemas
from pydantic.fields import Optional
from pydantic import BaseModel, EmailStr
from typing import List


class EmailBase(BaseModel):
    email: EmailStr


class EmailSchema(BaseModel):
    email: List[EmailStr]


class UserRead(schemas.BaseUser[int]):
    username: str
    role_id: int
    '''
    id: models.ID
    email: EmailStr
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False
    '''


class UserCreate(schemas.BaseUserCreate):
    username: str
    role_id: int
    '''
    email: str
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False
    '''


class UserUpdate(schemas.BaseUserUpdate):
    pass
