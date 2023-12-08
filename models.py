import os
from typing import Type

from sqlalchemy import create_engine
from sqlalchemy import DateTime, Integer, JSON, String
from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

engine = create_engine('sqlite:///users.db', echo=False)
metadata = MetaData()


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[str] = mapped_column(String(25))
    last_enter_date: Mapped[Type] = mapped_column(DateTime, nullable=True)
    interviews_duration: Mapped[int] = mapped_column(Integer)
    progress: Mapped[Type] = mapped_column(JSON)


def create_db() -> None:
    if not _is_db_crated():
        Base.metadata.create_all(engine)


def _is_db_crated() -> bool:
    return os.path.exists('./users.db')
