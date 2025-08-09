from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class Page(Base):
    __tablename__ = "pages"
    id = Column(Integer, primary_key=True)
    url = Column(Text, nullable=False, unique=True)
    name = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    ads = relationship("Ad", back_populates="page")

class Ad(Base):
    __tablename__ = "ads"
    id = Column(Integer, primary_key=True)
    page_id = Column(Integer, ForeignKey("pages.id"), nullable=False)
    library_id = Column(String(64), nullable=True)
    title = Column(Text, nullable=True)
    body = Column(Text, nullable=True)
    lang = Column(String(16), nullable=True)
    status = Column(String(32), nullable=True)  # Active/Inactive
    started_at = Column(DateTime, nullable=True)
    platforms = Column(String(128), nullable=True)  # csv
    cta = Column(String(64), nullable=True)

    page = relationship("Page", back_populates="ads")
    assets = relationship("Asset", back_populates="ad")

class Asset(Base):
    __tablename__ = "assets"
    id = Column(Integer, primary_key=True)
    ad_id = Column(Integer, ForeignKey("ads.id"), nullable=False)
    type = Column(String(16), nullable=False)  # image/video
    storage_key = Column(Text, nullable=True)  # path in S3/MinIO
    preview_url = Column(Text, nullable=True)  # public/proxy url
    hash = Column(String(64), nullable=True)   # pHash/dHash placeholder
    width = Column(Integer, nullable=True)
    height = Column(Integer, nullable=True)
    duration = Column(Integer, nullable=True)

    ad = relationship("Ad", back_populates="assets")
