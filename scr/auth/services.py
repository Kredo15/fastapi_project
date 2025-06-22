import os

from fastapi import status, HTTPException
from sqlalchemy import insert
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta

from scr.auth.dependencies import authenticate_user, get_user
from scr.auth.models import UsersOrm

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_access_token(form_data, db):
    user = await authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username})
    return access_token


async def create_user(user, db):
    db_user = get_user(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_password = get_password_hash(user.password)
    await db.execute(insert(UsersOrm).values(first_name=user.first_name,
                                             last_name=user.last_name,
                                             username=user.username,
                                             email=user.email,
                                             password=hashed_password,
                                             ))
    await db.commit()
    db.refresh(db_user)
    return db_user
