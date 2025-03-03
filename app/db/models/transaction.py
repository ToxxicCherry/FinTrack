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

class TransactionType(PyEnum):
    INCOME = "income"
    EXPENSE = "expense"


class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    amount = Column(Float, nullable=False)
    type = Column(Enum(TransactionType), nullable=False)
    date = Column(DateTime, default=datetime.utcnow())

    user = relationship("User", back_populates="transactions")
    category = relationship("Category")