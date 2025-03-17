from sqlalchemy import Column, Float, DateTime, ForeignKey, Enum, Text, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base
from app.models.user import BaseMixin
from app.enums import OrderStatus, LanguagePair

class Order(Base, BaseMixin):
    __tablename__ = "orders"
    
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime)
    price = Column(Float, nullable=False)
    status = Column(Enum(OrderStatus), default=OrderStatus.PENDING)
    target_url = Column(Text, nullable=False)
    language_pair = Column(Enum(LanguagePair), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    user = relationship("User", back_populates="orders")