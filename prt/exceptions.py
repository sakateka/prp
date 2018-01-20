"""
Известные ошибки при обработке классов
"""

class ScoreError(Exception):
    """Значнеие оценки вне допустимого диапазона, допуcтимые оценки от 1 до 5"""

class ExamPropertyError(Exception):
    """Ошибка установки полей класса Exam"""

class ExamDateError(Exception):
    """Не правильная дата сдачи экзамена"""
