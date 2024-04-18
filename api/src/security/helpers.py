from datetime import datetime, timedelta, timezone
from typing import Annotated, Dict, Literal

import bcrypt
from api.deps import get_db
from auth_token.token_model import TokenData
from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from jose.constants import ALGORITHMS
from security.oauth2 import oauth2_scheme
from settings.config import Settings, get_settings
from sqlalchemy.orm import Session
from user.user_crud import get_user_by_email
from user.user_model import User


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(bytes(plain_password, "utf-8"), bytes(hashed_password, "utf-8"))  # type: ignore[no-any-return]


def authenticate_user(db: Session, email: str, password: str) -> User | Literal[False]:
    user = get_user_by_email(db, email)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_access_token(
    data: Dict[str, str | datetime],
    secret_key: str,
    algorithm: str = ALGORITHMS.HS256,
    expires_delta: timedelta | None = None,
) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=algorithm)
    return encoded_jwt  # type: ignore[no-any-return]


ret_key: str


async def get_current_user(
    settings: Annotated[Settings, Depends(get_settings)],
    token: Annotated[str, Depends(oauth2_scheme)],
    db: Session = Depends(get_db),
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token, settings.secret_key, algorithms=[settings.algorithm]
        )
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user_by_email(db, token_data.username)
    if user is None:
        raise credentials_exception
    return user
