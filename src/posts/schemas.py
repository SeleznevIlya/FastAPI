from pydantic import BaseModel, Field
from datetime import datetime


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
