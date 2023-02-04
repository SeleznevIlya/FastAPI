from fastapi_users.db import SQLAlchemyBaseUserTable
from src.database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, JSON
from sqlalchemy.orm import relationship
from datetime import datetime


class Role(Base):
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    permissions = Column(JSON)


class User(SQLAlchemyBaseUserTable[int], Base):
    id = Column(Integer, primary_key=True, unique=True)
    username = Column(String, nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    role_id = Column(Integer, ForeignKey(Role.id))
    role = relationship("Role", back_populates="user")
