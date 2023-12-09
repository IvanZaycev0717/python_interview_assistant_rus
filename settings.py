from enum import Enum

# App setup
APP_NAME = 'Python Interview Assistant'
APP_RESOLUTION = (1280, 720)
CREATE_USER_WINDOW = 'Добавить пользователя'
HINT_WINDOW_TITLE = 'Подсказка'

# Validator section
WRONG_SYMBOLS = (
    '#', '@', '!', '?', '<', '>', '/',
    '|', '$', '^', '*', '(', ')', '+', '-', '='
    )

# Database name
DATABASE_NAME = 'users.db'

class ValidResponse(str, Enum):
    SUCCESS = '*Пользователь успешно создан'
    EMPTY_NAME = '*Имя пользователя не может быть пустой строкой'
    SHORT_NAME = '*Имя должно состоять минимум из двух символов'
    WRONG_FIRST_SYMBOL = '*Имя должно начинаться с буквы'
    WRONG_SYMBOLS = '*Имя содержит недопустимые символы'
    NAME_TOO_LONG = '*Имя должно содержать не более 25 символов'
    USER_ALREADY_EXISTS = '*Пользователь с таким именем уже существует'


class Theme(str, Enum):
    BASICS = 'Базовый синтаксис Python'
    OOP = 'Объекто-ориентированное программирование (ООП)'
    PEP8 = 'Правила оформления кода (PEP8, PEP257)'
    STRUCTURES = 'Структуры данных на Python'
    ALGHORITMS = 'Алгоритмы на Python'
    GIT = 'Git'
    SQL = 'Базы данных и SQL запросы'


class QuestionThreshold(int, Enum):
    BASIC_FIRST_QUESTION = 8
    BASIC_LAST_QUESTION = 224

    OOP_FIRST_QUESTION = 225
    OOP_LAST_QUESTION = 335

    PEP8_FIRST_QUESTION = 336
    PEP8_LAST_QUESTION = 363

    STRUCTURES_FIRST_QUESTION = 364
    STRUCTURES_LAST_QUESTION = 433

    ALGHORITMS_FIRST_QUESTION = 434
    ALGHORITMS_LAST_QUESTION = 473

    GIT_FIRST_QUESTION = 474
    GIT_LAST_QUESTION = 538

    SQL_FIRST_QUESTION = 539
    SQL_LAST_QUESTION = 597
