from typing import Optional

import bcrypt
from settings.config import get_settings
from sqlalchemy.orm import Session
from user.user_model import User
from user.user_schemas import UserCreate, UserUpdate

settings = get_settings()


def get_password_hash(password: str) -> str:
    return bcrypt.hash(password, bcrypt.gensalt())  # type: ignore[no-any-return]


def get_user_by_id(db: Session, id: int) -> Optional[User]:
    return db.query(User).filter(User.id == id).first()  # type: ignore[no-any-return]


def get_user_by_email(db: Session, email: str) -> Optional[User]:
    return db.query(User).filter(User.email == email).first()  # type: ignore[no-any-return]


def create_user(db: Session, create: UserCreate) -> User:
    password = get_password_hash(create.password)
    db_user = User(email=create.email, password=password)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def remove_user_by_id(db: Session, id: int) -> Optional[User]:
    db_user = db.query(User).filter(User.id == id).first()

    db.delete(db_user)
    db.commit()
    return db_user  # type: ignore[no-any-return]


def update_user_by_id(db: Session, id: int, update: UserUpdate) -> Optional[User]:
    db_user = db.query(User).filter(User.id == id).first()
    db_user.email = update.email
    db_user.password = update.password

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user  # type: ignore[no-any-return]
