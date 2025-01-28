from pydantic import EmailStr, BaseModel, Field, model_validator
from typing_extensions import Self
from datetime import datetime
from sqlmodel import UniqueConstraint, SQLModel


class UserBase(BaseModel):
    username: str = Field(min_length=4, max_length=20)


class UserAuth(UserBase):
    password: str = Field(min_length=8, max_length=14)


class UserCreate(UserAuth):
    email: EmailStr
    password_confirm: str

    @model_validator(mode="after")
    def password_match(self) -> Self:
        if self.password != self.password_confirm:
            raise ValueError("Password does not match")
        return self


class User(UserBase, SQLModel, table=True):
    __table_args__ = (UniqueConstraint("id", "email"),)
    id: int | None = Field(primary_key=True, default=None)
    email: EmailStr
    createdAt: datetime | None = datetime.now()
    updatedAt: datetime | None = datetime.now()
