from fastapi import APIRouter, status, HTTPException
from fastapi.params import Depends
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

from shortener.exceptions import URLHashNotFoundError
from shortener.services import URLShortenerService

router = APIRouter()


class URLToShort(BaseModel):
    url: str


@router.post("/")
async def short_url(url: URLToShort, service: URLShortenerService = Depends()):
    url_hash = await service.short_url(url.url)
    return {"url_hash": url_hash}


@router.get("/{url_hash}", response_class=RedirectResponse, status_code=status.HTTP_302_FOUND)
async def redirect_to_url(url_hash: str, service: URLShortenerService = Depends()):
    try:
        return await service.get_url_by_hash(url_hash)
    except URLHashNotFoundError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Url hash does not exist") 
