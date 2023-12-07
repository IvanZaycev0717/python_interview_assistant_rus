import datetime
from typing import TypedDict

from settings import QuestionThreshold as qt


class StatInformation(TypedDict):
    right_answers_amount: str
    percentage_completion: str
    basic_progress: float
    oop_progress: float
    pep_progress: float
    structures_progress: float
    alghorimts_progress: float
    git_progress: float
    sql_progress: float


def get_right_answers_amount(progress: dict) -> StatInformation:
    # Summary progress
    right_answers_amount = len([right for right in progress.values() if right])
    amount_of_answers = max(progress) - 7
    percentage_completion = (
        f'{round(100 * right_answers_amount / amount_of_answers, 1)}%'
        )

    # Patricular progress
    basic_amount = qt.BASIC_LAST_QUESTION - qt.BASIC_FIRST_QUESTION
    oop_amount = qt.OOP_LAST_QUESTION - qt.OOP_FIRST_QUESTION
    pep_amount = qt.PEP8_LAST_QUESTION - qt.PEP8_FIRST_QUESTION
    structures_amount = (
        qt.STRUCTURES_LAST_QUESTION - qt.STRUCTURES_FIRST_QUESTION
        )
    alghorimts_amount = (
        qt.ALGHORITMS_LAST_QUESTION - qt.ALGHORITMS_FIRST_QUESTION
        )
    git_amount = qt.GIT_LAST_QUESTION - qt.GIT_FIRST_QUESTION
    sql_amount = qt.SQL_LAST_QUESTION - qt.SQL_FIRST_QUESTION

    basic_progress = get_paticular_progress(
        progress, basic_amount, qt.BASIC_FIRST_QUESTION, qt.BASIC_LAST_QUESTION
        )
    oop_progress = get_paticular_progress(
        progress, oop_amount, qt.OOP_FIRST_QUESTION, qt.OOP_LAST_QUESTION
        )
    pep_progress = get_paticular_progress(
        progress, pep_amount, qt.PEP8_FIRST_QUESTION, qt.PEP8_LAST_QUESTION
        )
    structures_progress = get_paticular_progress(
        progress, structures_amount,
        qt.STRUCTURES_FIRST_QUESTION,
        qt.STRUCTURES_LAST_QUESTION
        )
    alghorimts_progress = get_paticular_progress(
        progress,
        alghorimts_amount,
        qt.ALGHORITMS_FIRST_QUESTION,
        qt.ALGHORITMS_LAST_QUESTION
        )
    git_progress = get_paticular_progress(
        progress, git_amount, qt.GIT_FIRST_QUESTION, qt.GIT_LAST_QUESTION
        )
    sql_progress = get_paticular_progress(
        progress, sql_amount, qt.SQL_FIRST_QUESTION, qt.SQL_LAST_QUESTION
        )

    return StatInformation(
        right_answers_amount=f'{right_answers_amount} из {amount_of_answers}',
        percentage_completion=percentage_completion,
        basic_progress=basic_progress,
        oop_progress=oop_progress,
        pep_progress=pep_progress,
        structures_progress=structures_progress,
        alghorimts_progress=alghorimts_progress,
        git_progress=git_progress,
        sql_progress=sql_progress,
        )


def get_last_enter_message(date: datetime) -> str:
    return f'{date.day}.{date.month}.{date.year}'


def get_paticular_progress(
        user_progress: dict, amount_kind: int, from_: int, to_: int) -> float:
    return round(
        len(
            [is_right for question_number, is_right in user_progress.items()
             if question_number
             in range(from_, to_) and is_right]) / amount_kind, 1
             )
