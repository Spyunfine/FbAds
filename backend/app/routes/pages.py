from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import Page
from pydantic import BaseModel, HttpUrl

router = APIRouter(prefix="/pages", tags=["pages"])

class PageIn(BaseModel):
    url: HttpUrl

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("")
def add_page(payload: PageIn, db: Session = Depends(get_db)):
    exists = db.query(Page).filter(Page.url == str(payload.url)).first()
    if exists:
        return {"id": exists.id, "url": exists.url}
    page = Page(url=str(payload.url))
    db.add(page)
    db.commit()
    db.refresh(page)
    return {"id": page.id, "url": page.url}

@router.get("")
def list_pages(db: Session = Depends(get_db)):
    pages = db.query(Page).order_by(Page.id.desc()).all()
    return [{"id": p.id, "url": p.url, "created_at": p.created_at.isoformat()} for p in pages]
