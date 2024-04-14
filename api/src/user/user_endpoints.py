from datetime import timedelta
from typing import Annotated, Optional

from api.deps import get_db
from auth_token.token_model import Token
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from security.helpers import authenticate_user, create_access_token
from security.oauth2 import oauth2_scheme
from settings.config import Settings, get_settings
from sqlalchemy.orm import Session
from user import user_crud, user_schemas
from user.user_model import User

router = APIRouter()


@router.post("/token")  # type: ignore[misc]
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db),
    settings: Settings = Depends(get_settings),
) -> Token:
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    access_token = create_access_token(
        data={"sub": user.email},
        secret_key=settings.secret_key,
        expires_delta=access_token_expires,
    )
    return Token(access_token=access_token, token_type="bearer")


@router.post("/", response_model=user_schemas.User)  # type: ignore[misc]
async def create_user(
    *,
    db: Session = Depends(get_db),
    create: user_schemas.UserCreate,
) -> User:
    """
    Create a new user.
    """
    user = user_crud.create_user(db=db, create=create)
    return user


@router.get("/{id}", response_model=user_schemas.User)  # type: ignore[misc]
async def get_user_by_id(
    *,
    db: Session = Depends(get_db),
    id: int,
) -> User:
    """
    Get user by ID.
    """
    user = user_crud.get_user_by_id(db=db, id=id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found."
        )
    return user


@router.get("/email", response_model=user_schemas.User)  # type: ignore[misc]
async def get_user_by_email(
    *,
    db: Session = Depends(get_db),
    email: str,
) -> User:
    """
    Get user by email.
    """
    user = user_crud.get_user_by_email(db=db, email=email)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No user with that email."
        )
    return user


@router.put("/{id}", response_model=user_schemas.User)  # type: ignore[misc]
async def update_user_by_id(
    *,
    token: Annotated[str, Depends(oauth2_scheme)],
    db: Session = Depends(get_db),
    id: int,
    update: user_schemas.UserUpdate,
) -> Optional[User]:
    """
    Update an user by ID.
    """
    user = user_crud.get_user_by_id(db=db, id=id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found."
        )
    user = user_crud.update_user_by_id(db=db, id=id, update=update)
    return user


@router.delete("/{id}", response_model=user_schemas.User)  # type: ignore[misc]
async def delete_user(
    *,
    token: Annotated[str, Depends(oauth2_scheme)],
    db: Session = Depends(get_db),
    id: int,
) -> Optional[User]:
    """
    Delete an user by ID.
    """
    user = user_crud.get_user_by_id(db=db, id=id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found."
        )
    user = user_crud.remove_user_by_id(db=db, id=id)
    return user
