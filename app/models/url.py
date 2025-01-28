from datetime import datetime
from pydantic import BaseModel
from sqlmodel import SQLModel, Field
from sqlalchemy import UniqueConstraint


class UrlBase(BaseModel):
    url: str
    createdAt: datetime | None = datetime.now()
    updatedAt: datetime | None = datetime.now()


class Url(UrlBase, SQLModel, table=True):
    __table_args__ = (UniqueConstraint("id", "url", "shortCode"),)
    id: int | None = Field(primary_key=True, default=None)
    shortCode: str
    visits: int | None = 0
