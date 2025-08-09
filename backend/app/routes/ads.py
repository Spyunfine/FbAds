from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import Ad, Asset

router = APIRouter(prefix="/creatives", tags=["creatives"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("")
def list_creatives(db: Session = Depends(get_db)):
    ads = db.query(Ad).order_by(Ad.id.desc()).limit(100).all()
    results = []
    for ad in ads:
        assets = [
            {
                "id": a.id,
                "type": a.type,
                "preview_url": a.preview_url,
            }
            for a in ad.assets
        ]
        results.append({
            "ad_id": ad.id,
            "library_id": ad.library_id,
            "status": ad.status,
            "started_at": ad.started_at.isoformat() if ad.started_at else None,
            "platforms": ad.platforms,
            "title": ad.title,
            "body": ad.body,
            "lang": ad.lang,
            "cta": ad.cta,
            "assets": assets
        })
    return results
