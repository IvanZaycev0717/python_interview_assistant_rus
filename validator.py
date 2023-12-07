from manage_db import get_user_names
from settings import WRONG_SYMBOLS


def is_name_empty(user_name: str) -> bool:
    return len(user_name) == 0


def is_name_too_short(user_name: str) -> bool:
    return len(user_name) < 2


def has_name_first_wrong_symbol(user_name: str) -> bool:
    return user_name[0] in (' ', *WRONG_SYMBOLS, *map(str, range(10)))


def has_name_wrong_symbols(user_name: str) -> bool:
    return any({symbol in WRONG_SYMBOLS for symbol in user_name})


def is_name_too_long(user_name: str) -> bool:
    return len(user_name) > 25


def is_user_already_exists(user_name: str) -> bool:
    return user_name in get_user_names()
