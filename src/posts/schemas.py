from pydantic import BaseModel, Field
from datetime import datetime
from src.auth.schemas import UserRead


class Category(BaseModel):
    category_name: str


class PostBase(BaseModel):
    header: str
    content: str
    datetime: datetime
    category_id: list[Category]

    class Config:
        orm_mode = True


class PostList(PostBase):
    id: int


class PostCreate(BaseModel):
    pass


class PostUpdate(BaseModel):
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
