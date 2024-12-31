from datetime import datetime
from pydantic import BaseModel


class Url(BaseModel):
    id: int
    url: str
    shortCode: str
    createdAt: datetime | None = datetime.now()
    updatedAt: datetime | None = datetime.now()
    visits: int | None = 0
