from typing import Literal


from sqlalchemy import insert, select


from models import *
from settings import QuestionThreshold as qt


def create_new_user(user_name):
    with engine.connect() as conn:
        conn.execute(
        insert(User).values(
        user_name=user_name,
        last_enter_date=datetime.datetime.now(),
        last_action_date=datetime.datetime.now(),
        interviews_duration=0,
        progress=_get_zero_progress()
        )
        )
        conn.commit()


def get_users_list() -> list[tuple[str]]:
    with engine.connect() as conn:
        result = conn.execute(select(User.user_name))
        conn.commit()
    return result.all()


def _get_zero_progress() -> json:
    return json.dumps(_create_zero_progress())


def _create_zero_progress() -> dict[Literal['question number'], bool]:
    return {
        question_number: False for question_number
        in range(qt.BASIC_FIRST_QUESTION, qt.SQL_LAST_QUESTION + 1)
        }