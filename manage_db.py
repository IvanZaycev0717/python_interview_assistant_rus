import datetime
import json

from sqlalchemy import delete, insert, select, update

from models import engine, User
from settings import QuestionThreshold as qt


# user_name column
def create_new_user(user_name: str) -> None:
    with engine.connect() as conn:
        conn.execute(insert(User).values(
            user_name=user_name,
            interviews_duration=0,
            progress=_get_zero_progress()
            )
            )
        conn.commit()


def get_user_names() -> list[str]:
    names = get_users_list()
    return [person for name in names for person in name]


def get_users_list() -> list[tuple[str]]:
    with engine.connect() as conn:
        result = conn.execute(select(User.user_name))
        conn.commit()
    return result.all()


def delete_this_user(user_name: str) -> None:
    with engine.connect() as conn:
        conn.execute(delete(User).where(User.user_name == user_name))
        conn.commit()


# last_enter_date Column
def get_last_enter_date(user_name: str) -> datetime.datetime:
    with engine.connect() as conn:
        result = conn.execute(
            select(User.last_enter_date).where(
                User.user_name == user_name)).first()
        conn.commit()
    return result[0]


def update_last_enter_date(user_name: str, date) -> None:
    with engine.connect() as conn:
        conn.execute(
            update(User).where(
                User.user_name == user_name).values(last_enter_date=date))
        conn.commit()


# interview_duration Column
def get_user_interview_duration(user_name: str) -> int:
    with engine.connect() as conn:
        interview_duration = conn.execute(
            select(User.interviews_duration
                   ).where(User.user_name == user_name)
                   ).first()
        conn.commit()
    return int(interview_duration[0])


def update_interview_duration(user_name: str, duration) -> None:
    with engine.connect() as conn:
        conn.execute(
            update(User).where(
                User.user_name == user_name).values(
                    interviews_duration=duration
                    )
                    )
        conn.commit()


# progress Column
def get_user_progress(
        user_name: str) -> dict[int, bool]:
    progress = json.loads(load_user_progress(user_name))
    return {
        int(question_number): is_rigth
        for question_number, is_rigth in progress.items()
        }


def load_user_progress(user_name: str) -> str:
    with engine.connect() as conn:
        result = conn.execute(select(User.progress).where(
            User.user_name == user_name))
        conn.commit()
    return result.all()[0][0]


def update_user_progress(user_name: str, progress: dict) -> None:
    with engine.connect() as conn:
        conn.execute(
            update(User).where(
                User.user_name == user_name).values(
                    progress=json.dumps(progress)))
        conn.commit()


# Support functions
def _get_zero_progress() -> str:
    return json.dumps(_create_zero_progress())


def _create_zero_progress() -> dict[int, bool]:
    return {
        question_number: False for question_number
        in range(qt.BASIC_FIRST_QUESTION, qt.SQL_LAST_QUESTION + 1)
    }
