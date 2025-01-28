from app.db.db import SessionDep
from app.models.url import Url
from sqlmodel import select
from hashlib import md5


def exist_url(url: str, session: SessionDep) -> Url | None:

    url_db = session.exec(
        select(Url).where(
            Url.url == url
        )
    ).first()

    if url_db:
        return url_db

    return None


def hash_url(url: str, session: SessionDep) -> str:
    url_hash = md5(url.encode()).hexdigest()
    url_hash = url_hash[:4]

    url_db = session.exec(
        select(Url).where(
            Url.shortCode.startswith(url_hash)
        )
    ).first()

    if url_db:
        increment = int(url_db.shortCode.split("+")[1]) + 1
        return f"{url_hash}+{increment}"

    return url_hash
