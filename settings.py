from enum import Enum

class Theme(Enum):
    BASICS = 'Базовый синтаксис Python'
    OOP = 'Объекто-ориентированное программирование (ООП)'
    PEP8 = 'Правила оформления кода (PEP8, PEP257)'
    STRUCTURES = 'Структуры данных на Python'
    ALGHORITMS = 'Алгоритмы на Python'
    GIT = 'Git'
    SQL = 'Базы данных и SQL запросы'

class QuestionThreshold(Enum):
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


