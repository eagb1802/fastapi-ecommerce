from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker
from src.core.config import settings
from typing import Iterator
import logging

engine = create_engine(settings.database_url)

SessionLocal = sessionmaker(bind=engine, autoflush=False)

Base = declarative_base()

logger = logging.getLogger('uvicorn.error')


def get_db() -> Iterator[Session]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
