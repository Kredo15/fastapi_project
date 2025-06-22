from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from scr.database.db import get_async_session

from scr.auth.services import get_access_token, create_user
from scr.auth.schemas import UsersAddSchema

router = APIRouter(prefix='/auth', tags=['auth'])


@router.post("/sign-in")
async def login_for_access_token(
        data_user: OAuth2PasswordRequestForm = Depends(),
        db: Session = Depends(get_async_session)):
    access_token = get_access_token(data_user, db)
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/sign-up")
async def signup(data_user: UsersAddSchema, db: Session = Depends(get_async_session)):
    await create_user(data_user, db)
    return {'status': '201', 'data': {'messages': ['User successfully created!']}}
