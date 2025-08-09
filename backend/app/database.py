from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import POSTGRES_DSN

engine = create_engine(POSTGRES_DSN, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def init_db():
    from . import models  # noqa
    Base.metadata.create_all(bind=engine)
