from pydantic import BaseModel
from datetime import datetime

from app.models.enums import TransactionType

class TransactionBase(BaseModel):
    amount: float
    type: TransactionType
    description: str | None = None

class TransactionCreate(TransactionBase):
    pass

class TransactionResponse(TransactionBase):
    id: int
    created_at: datetime
    user_id: int
    
    class Config:
        orm_mode = True
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }