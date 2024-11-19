from fastapi import FastAPI, Depends, HTTPException, File, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncSession
from .db.db import get_session, create_tables
from .db.models import UserLogin

from .schema import UserCred, LoginSuccess, SignUpSuccess
from .auth.auth import Auth, get_current_user, add_user, get_current_user_from_token


app = FastAPI()
auth = Auth()


@app.on_event("startup")
async def on_startup():
    await create_tables()


@app.post("/login", response_model=LoginSuccess)
async def login(user: UserCred, session: AsyncSession = Depends(get_session)):
    usercheck = await get_current_user(session, user.email)
    if usercheck is None or not auth.verify_password(
        user.password, usercheck.hashed_password
    ):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = auth.create_token(user.email)
    return {"access_token": access_token, "token_type": "Bearer"}


@app.post("/signup", response_model=SignUpSuccess)
async def signup(user: UserCred, session: AsyncSession = Depends(get_session)):
    usercheck = await get_current_user(session, user.email)
    if usercheck:
        raise HTTPException(status_code=400, detail="User already exists")
    await add_user(session, user.email, user.password)
    return {"message": True}
