import os
from typing import Type

from sqlalchemy import create_engine
from sqlalchemy import DateTime, Integer, JSON, String
from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from settings import DATABASE_NAME

engine = create_engine(f'sqlite:///{DATABASE_NAME}', echo=False)
metadata = MetaData()


class Base(DeclarativeBase):
    pass


class User(Base):
    """A class representing user's data in the app.

    Attributes:
        __tablename__ (str): The name of the table in the database.
        id: The unique identifier of the user.
        user_name: The name of the user.
        last_enter_date: The date and time of the user's last login.
        interviews_duration: The total duration of interviews
        for the user in seconds.
        progress: The user's progress data stored in JSON format.
    """
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[str] = mapped_column(String(25))
    last_enter_date: Mapped[Type] = mapped_column(DateTime, nullable=True)
    interviews_duration: Mapped[int] = mapped_column(Integer)
    progress: Mapped[Type] = mapped_column(JSON)


def create_db() -> None:
    """Creates database as a SQLite-file"""
    if not _is_db_created():
        Base.metadata.create_all(engine)


def _is_db_created() -> bool:
    """Checks DB existence in the root folder."""
    return os.path.exists(f'./{DATABASE_NAME}')
