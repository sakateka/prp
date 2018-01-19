#!/usr/bin/env python3
"""
Основной исполняемый файл программы.
"""

import argparse
import logging
from prt import report

logging.basicConfig(level=logging.INFO)

def main():
    """
    Функция разбора аргументов и запуска основной функциональности программы
    """
    parser = argparse.ArgumentParser("Отчёт средней оценки инструктора")
    parser.add_argument("source", help="Файл с результатами экзаменов (в формате json)")
    parser.add_argument("report", help="Имя файла для записи отчёта")
    parser.add_argument(
        "-d", "--debug",
        help="Выводить подробный лог действий", action="store_true"
    )
    args = parser.parse_args()
    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)

    report.build(args)

if __name__ == "__main__":
    main()
