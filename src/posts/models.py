from sqlalchemy import Column, String, Integer, TIMESTAMP,  JSON, ForeignKey, DateTime
from datetime import datetime
from database import Base
from auth.models import User
from sqlalchemy.orm import relationship


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, unique=True)
    category_name = Column(String, unique=True)

    post = relationship('Post', secondary="post_category", back_populates='category')


class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True, unique=True)
    header = Column(String, unique=True)
    content = Column(String)
    datetime = Column(DateTime, default=datetime.now())
    category_id = Column(Integer, ForeignKey("category.id"))
    user_id = Column(Integer, ForeignKey(User.id))
    rating = Column(Integer, default=0)

    user = relationship('User', back_populates="post")
    category = relationship('Category', secondary="post_category", back_populates='post')
    comment = relationship("Comment", back_populates="post")



class PostCategory(Base):
    __tablename__ = 'post_category'

    id = Column(Integer, primary_key=True, unique=True)
    post = Column(Integer, ForeignKey("post.id"))
    category = Column(Integer, ForeignKey("category.id"))


class Comment(Base):
    __tablename__ = "comment"

    id = Column(Integer, primary_key=True, unique=True)
    author_id = Column(Integer, ForeignKey("user.id"))
    post_id = Column(Integer, ForeignKey("post.id"))
    content = Column(String)
    datetime = Column(DateTime, default=datetime.now())
    rating = Column(Integer, default=0)

    post = relationship("Post", back_populates="comment")
