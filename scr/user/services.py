from datetime import datetime, timedelta, timezone
import os
from typing import Annotated

from fastapi import status, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert
from passlib.context import CryptContext
import jwt

from scr.database.db import get_async_session
from scr.user.schemas import UsersAddSchema
from scr.user.models import UsersOrm


bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')


async def authenticate_user(db: Annotated[AsyncSession,
                            Depends(get_async_session)], username: str, password: str):
    user = await db.scalar(select(UsersOrm).where(UsersOrm.username == username))
    if not user or not bcrypt_context.verify(password, user.hashed_password) or not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


async def create_access_token(username: str, user_id: int, is_administrator: bool,
                              is_active: bool, is_verified: bool, expires_delta: timedelta):
    encode = {'sub': username, 'id': user_id, 'is_administrator': is_administrator,
              'is_active': is_active, 'is_verified': is_verified}
    expires = datetime.now(timezone.utc) + expires_delta
    encode.update({"exp": expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


async def insert_user(db: Annotated[AsyncSession, Depends(get_async_session)], add_user: UsersAddSchema):
    await db.execute(insert(UsersOrm).values(first_name=add_user.first_name,
                                             last_name=add_user.last_name,
                                             username=add_user.username,
                                             email=add_user.email,
                                             password=bcrypt_context.hash(add_user.password),
                                             ))
    await db.commit()
