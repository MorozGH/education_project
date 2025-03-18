from pydantic import BaseModel, validator
from datetime import datetime
from typing import Optional
import re

from app.models.enums import LanguagePair, OrderStatus

class OrderBase(BaseModel):
    target_url: str
    language_pair: LanguagePair

    @validator("language_pair", pre=True)
    def lowercase_lang_pair(cls, v):
        if isinstance(v, str):
            return v.lower()
        return v

class OrderCreate(OrderBase):
    pass

class OrderUpdate(BaseModel):
    status: Optional[str]
    end_time: Optional[datetime]

class OrderResponse(OrderBase):
    id: int
    start_time: datetime
    end_time: Optional[datetime]
    price: float
    status: OrderStatus
    user_id: int
    
    class Config:
        orm_mode = True