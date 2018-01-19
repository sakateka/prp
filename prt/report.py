"""
Модуль, который выполняет построение отчёта
"""
import json
import logging
from collections import defaultdict
from .classes import Instructor, Student, Exam

LOG = logging.getLogger(__name__)

def parse_one_result(doc):
    """
    Функция для преобразования данных из файла результатов
    во внутреннее предсталвение программы
    """
    student = Student(
        doc["student"]["name"],
        doc["student"]["age"],
        doc["student"]["score"],
    )
    instructor = Instructor(
        doc["instructor"]["name"],
        doc["instructor"]["age"],
        doc["instructor"]["car"],
    )
    exam = Exam(instructor, student, doc["date"])
    LOG.debug("Добавляем результат экзамена: %s", exam)
    return exam


def collect_results(results_file):
    """
    Функция собирает результаты экзаменов,
    формируя из них объекты, используемые в программе
    """
    LOG.debug("Сбор результатов")

    results = []
    try:
        with open(results_file) as results_fd:
            current_result = 0
            for res in json.load(results_fd):
                current_result += 1
                try:
                    results.append(parse_one_result(res))
                except (IndexError, ValueError) as err:
                    LOG.error("Ошибка при чтении документа %s: %s", current_result, err)

    except IOError as exc:
        LOG.error("Ошибка при чтении результатов экзаменов: %s", exc)

    return results

def build(args):
    """
    Функция создания отчета
    """

    results = collect_results(args.source)
    report = defaultdict(list)
    for exam in results:
        report[exam.instructor.fio].append(exam.student.score)

    with open(args.report, "w+") as report_file:
        report_file.write(
            "".join(
                "{}: количество экзаменов = {}, средняя оценка = {:0.3f}\n".format(
                    name,
                    len(scores),
                    float(sum(scores))/len(scores),
                ) for name, scores in report.items()
            )
        )
