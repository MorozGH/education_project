from sqlalchemy import Column, Float, String, ForeignKey, Enum, Integer
from sqlalchemy.orm import relationship

from app.database import Base
from app.models.enums import TransactionType

from app.models.user import BaseMixin

class Transaction(Base, BaseMixin):
    __tablename__ = "transactions"
    
    amount = Column(Float, nullable=False)
    type = Column(Enum(TransactionType), nullable=False)
    description = Column(String(255))
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    user = relationship("User", back_populates="transactions")