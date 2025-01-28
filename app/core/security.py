from dotenv import load_dotenv
from os import getenv
from passlib.context import CryptContext
from fastapi.security import HTTPBearer
from typing import Annotated
from fastapi import Depends
import jwt
import json
from datetime import datetime, timedelta, timezone
from app.models.user import User

dotenv = load_dotenv()

ALGORITHM = "HS256"
SECRET_KEY = getenv("SECRET_KEY")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
security = HTTPBearer()

SecurityDep = Annotated[HTTPBearer, Depends(security)]


def create_access_token(data: User, expire: timedelta = timedelta(hours=1)) -> str:
    to_encode = {
        "exp": datetime.now(timezone.utc) + expire,
        "sub": json.dumps(data.model_dump())
    }
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_token(token: str) -> User:
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    user_dict = json.loads(payload.get("sub"))
    if user_dict is None:
        return None
    return User.model_validate(user_dict)
