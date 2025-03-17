from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.models.transaction import Transaction
from app.models.order import Order
from app.schemas.order import OrderCreate, OrderResponse
from app.dependencies import get_current_user

router = APIRouter(tags=["orders"])

@router.post("/orders/", response_model=OrderResponse)
def create_order(
    order: OrderCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.balance < 0.5:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Insufficient balance"
        )
    
    price = 0.5  # base cost for minute / for example
    
    db_order = Order(
        **order.dict(),
        price=price,
        user_id=current_user.id
    )
    
    transaction = Transaction(
        amount=-price,
        type="withdrawal",
        user_id=current_user.id
    )
    
    current_user.balance -= price
    
    try:
        db.add(db_order)
        db.add(transaction)
        db.commit()
        db.refresh(db_order)
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
    
    return db_order

@router.get("/orders/", response_model=list[OrderResponse])
def read_orders(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return db.query(Order)\
        .filter(Order.user_id == current_user.id)\
        .offset(skip)\
        .limit(limit)\
        .all()