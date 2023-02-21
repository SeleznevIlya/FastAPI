from fastapi_users.db import SQLAlchemyBaseUserTable
from database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, JSON
from sqlalchemy.orm import relationship
from datetime import datetime


class Role(Base):
    __tablename__ = 'role'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    permissions = Column(JSON)

    user = relationship("User", back_populates="role")


class User(SQLAlchemyBaseUserTable[int], Base):
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, unique=True)
    username = Column(String, nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    role_id = Column(Integer, ForeignKey(Role.id))

    role = relationship("Role", back_populates="user")
    post = relationship("Post", back_populates="user")
    '''
    email: str = Column(String(length=320), unique=True, index=True, nullable=False)
    hashed_password: str = Column(String(length=1024), nullable=False)
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)
    '''
