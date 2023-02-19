from sqlalchemy import Column, String, Integer, TIMESTAMP,  JSON, ForeignKey, DateTime
from datetime import datetime
from database import Base
from src.auth.models import User
from sqlalchemy.orm import relationship


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, unique=True)
    category_name = Column(String, unique=True)


class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True, unique=True)
    header = Column(String, unique=True)
    content = Column(String)
    datetime = Column(DateTime, default=datetime.now())
    category_id = Column(Integer, ForeignKey(Category.id))
    user_id = Column(Integer, ForeignKey(User.id))
    post_rating = Column(Integer, default=0)

    author = relationship('User', back_populates="post")
    category = relationship('Category', back_populates='post')


class PostCategory(Base):
    __tablename__ = 'post_category'

    id = Column(Integer, primary_key=True, unique=True)
    post = Column(Integer, ForeignKey(Post.id))
    category = Column(Integer, ForeignKey(Category.id))


class Comment(Base):
    __tablename__ = "comment"

    id = Column(Integer, primary_key=True, unique=True)
    author = Column(Integer, ForeignKey(User.id))
    post = Column(Integer, ForeignKey(Post.id))
    content = Column(Integer)
    datetime = Column(DateTime)
    comment_rating = Column(Integer, default=0)
