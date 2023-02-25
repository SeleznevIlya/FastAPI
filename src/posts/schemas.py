from pydantic import BaseModel, Field
from datetime import datetime
from auth.schemas import UserRead


class Category(BaseModel):
    category_name: str


class PostBase(BaseModel):
    header: str
    content: str
    datetime: datetime
    category_id: int
    user_id: int

    class Config:
        orm_mode = True


class PostList(PostBase):
    id: int


class PostCreate(BaseModel):
    header: str
    content: str
    category_id: int




class PostUpdate(PostCreate):
    pass


class CommentBase(BaseModel):
    content: str
    datetime: datetime
    comment_rating: int
    author: UserRead


class CommentList(CommentBase):
    pass


class CommentCreate(BaseModel):
    content: str


class CommentUpdate(CommentCreate):
    pass
