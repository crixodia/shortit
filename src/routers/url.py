from fastapi import APIRouter, Path
router = APIRouter()


@router.post("/{url}")
def short_url(url: str):
    pass


@router.get("/{url}")
def get_url():
    pass


@router.put("/{url}")
def update_url():
    pass


@router.delete("/{url}")
def delete_url():
    pass
