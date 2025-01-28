from fastapi import APIRouter, Path, Query, status, HTTPException
from fastapi.responses import RedirectResponse

from app.models.url import Url
from app.services.url import exist_url, hash_url
from app.db.db import SessionDep
from sqlalchemy import select

URL_REGEX = r"https?:\/\/(?:www\.)?([-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b)*(\/[\/\d\w\.-]*)*(?:[\?])*(.+)*"

router = APIRouter(
    prefix="/",
    tags=["url"],
)


@router.get(status_code=status.HTTP_201_CREATED)
async def short_url(session: SessionDep, url: str = Query(str, regex=URL_REGEX)) -> Url:
    validate_url = exist_url(url)
    if validate_url:
        return validate_url

    url_hash = hash_url(url)
    url_db = Url.model_validate(url=url, url_hash=url_hash)

    session.add(url_db)
    session.commit()
    session.refresh(url_db)

    return url_db


@router.get(status_code=status.HTTP_302_FOUND)
def get_url(session: SessionDep, short_code: str = Query(str, min_length=4)) -> str:
    url = session.exec(select(Url).where(Url.url_hash == short_code)).first()
    if not url:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="URL not found"
        )

    return RedirectResponse(url.url)


@router.put(status_code=status.HTTP_501_NOT_IMPLEMENTED)
def update_url() -> dict:
    return {"message": "Not implemented"}


@router.delete(status_code=status.HTTP_501_NOT_IMPLEMENTED)
def delete_url() -> dict:
    return {"message": "Not implemented"}
