from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker
from src.core.config import settings
from typing import Iterator

engine = create_engine(settings.database_url)

SessionLocal =sessionmaker(bind=engine, autoflush=False)

Base = declarative_base()

def get_db() -> Iterator[Session]:

    db = SessionLocal()

    try:
        pass

        yield db
    except:
        pass
    finally:
        db.close()
