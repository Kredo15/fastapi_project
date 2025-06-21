from typing import Annotated

from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from scr.database.db import get_async_session
from scr.user.schemas import UsersAddSchema
from scr.user.services import insert_user


router = APIRouter(prefix='/auth', tags=['auth'])


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_user(db: Annotated[AsyncSession, Depends(get_async_session)], add_user: UsersAddSchema):
    await insert_user(db, add_user)
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful'
    }
