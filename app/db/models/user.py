from app.db import Base
from sqlalchemy import (
Integer,
String,
ForeignKey,
Column,
Float,
Boolean,
DateTime,
Enum
)
from sqlalchemy.orm import relationship
from datetime import datetime
from enum import Enum as PyEnum


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    transactions = relationship("Transaction", back_populates="user")