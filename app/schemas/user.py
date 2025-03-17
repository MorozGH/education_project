from pydantic import BaseModel, EmailStr, validator
from datetime import datetime
from typing import Optional

from app.schemas.transaction import TransactionResponse

class UserBase(BaseModel):
    email: EmailStr
    full_name: str

class UserCreate(UserBase):
    password: str
    phone_number: Optional[str] = None
    
    @validator('password')
    def validate_password(cls, v):
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters")
        return v

class UserUpdate(UserBase):
    phone_number: Optional[str] = None

class UserInDB(UserBase):
    id: int
    is_active: bool
    balance: float
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }

class UserPublic(UserInDB):
    pass

class UserWithTransactions(UserPublic):
    transactions: list['TransactionResponse'] = []