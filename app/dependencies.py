from fastapi import Cookie, Depends, HTTPException, status
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from typing import Optional

from app.database import get_db
from app.models.user import User
from app.security import SECRET_KEY, ALGORITHM

async def get_current_user(
    session: Optional[str] = Cookie(None, alias="session"),
    db: Session = Depends(get_db)
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    if not session:
        raise credentials_exception

    try:
        # Удаляем лишние кавычки и префикс Bearer
        token = session.strip('"').replace("Bearer ", "")
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError as e:
        raise credentials_exception from e

    user = db.query(User).filter(User.email == email).first()
    if user is None:
        raise credentials_exception
        
    return user

async def get_optional_user(
    session: Optional[str] = Cookie(None, alias="session"),
    db: Session = Depends(get_db)
) -> Optional[User]:
    try:
        return await get_current_user(session, db)
    except HTTPException:
        return None