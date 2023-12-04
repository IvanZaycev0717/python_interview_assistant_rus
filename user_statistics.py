import datetime


from typing import TypedDict

from settings import QuestionThreshold as qt

class StatInformation(TypedDict):
    right_answers_amount: str
    percentage_completion: str


def get_right_answers_amount(progress: dict) -> StatInformation:

    global user_progress
    user_progress=progress

    # Summary progress
    right_answers_amount = sum([1 for right in progress.values() if right])
    amount_of_answers = max(progress)
    percentage_completion = f'{round(100 * right_answers_amount / amount_of_answers, 1)}%'
    
    # Patricular progress
    basic_amount = qt.BASIC_LAST_QUESTION - qt.BASIC_FIRST_QUESTION
    oop_amount = qt.OOP_LAST_QUESTION - qt.OOP_FIRST_QUESTION
    pep_amount = qt.PEP8_LAST_QUESTION - qt.PEP8_FIRST_QUESTION
    structures_amount = qt.STRUCTURES_LAST_QUESTION - qt.STRUCTURES_FIRST_QUESTION
    alghorimts_amount = qt.ALGHORITMS_LAST_QUESTION - qt.ALGHORITMS_FIRST_QUESTION
    git_amount = qt.GIT_LAST_QUESTION - qt.GIT_FIRST_QUESTION
    sql_amount = qt.SQL_LAST_QUESTION - qt.SQL_FIRST_QUESTION

    basic_progress = round(
        sum(
        [1 for right in progress.values()
         if right and progress.keys() in range(qt.BASIC_FIRST_QUESTION, qt.BASIC_LAST_QUESTION + 1)]
        ) / basic_amount, 1
        )

    oop_progress = round(
        sum(
        [1 for right in progress.values()
         if right and progress.keys() in range(qt.OOP_FIRST_QUESTION, qt.OOP_LAST_QUESTION + 1)]
        ) / oop_amount, 1
        )
    
    pep_progress = round(
        sum(
        [1 for right in progress.values()
         if right and progress.keys() in range(qt.PEP8_FIRST_QUESTION, qt.PEP8_LAST_QUESTION + 1)]
        ) / pep_amount, 1
        )
    

    
    return StatInformation(
        right_answers_amount= f'{right_answers_amount} из {amount_of_answers}',
        percentage_completion=percentage_completion
        )

def get_last_enter_message(date: datetime) -> str:
    return f'{date.day}.{date.month}.{date.year}'

def get_paticular_amount(amount_kind: int, from_: int, to_: int) -> float:
    round(
        sum(
        [1 for right in user_progress.values()
         if right and user_progress.keys() in range(from_, to_ + 1)]
        ) / amount_kind, 1
        )
