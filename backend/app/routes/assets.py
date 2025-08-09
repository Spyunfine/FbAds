from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import Asset
from ..s3 import presigned_get

router = APIRouter(prefix="/assets", tags=["assets"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{asset_id}/download")
def download_asset(asset_id: int, db: Session = Depends(get_db)):
    asset = db.query(Asset).get(asset_id)
    if not asset or not asset.storage_key:
        raise HTTPException(status_code=404, detail="Asset not found")
    url = presigned_get(asset.storage_key, expires=3600)
    return {"url": url}
