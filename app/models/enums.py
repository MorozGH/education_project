from enum import Enum

class TransactionType(str, Enum):
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"

class OrderStatus(str, Enum):
    PENDING = "pending"
    ACTIVE = "active"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class LanguagePair(str, Enum):
    EN_RU = "en-ru"
    RU_DE = "ru-en"