r"""
Описание классов.
Иерархия классов следующая

      +---------+
      | Человек |
      +---------+
        /      \
 +--------+  +------------+
 | Ученик |  | Инструктор |
 +--------+  +------------+
"""

class Person():
    """
    Класс описания человека
    ФИО и возраст устанавливаются один раз на этапе создания класса,
    и дальнейшее их изменение не предусмотрено.
    Поэтому для этих полей нет методов изменяющих их значение.
    """
    def __init__(self, fio, age):
        self._fio = fio
        self._age = age

    @property
    def fio(self):
        """Метод для получения значения ФИО"""
        return self._fio

    @property
    def age(self):
        """Метод для установки значения возраста"""
        return self._age


class Instructor(Person):
    """
    Инструктор автошколы
    """
    def __init__(self, fio, age, car):
        # Инициализация полей родительского класса
        super(Instructor, self).__init__(fio, age)
        # Инициализация собственных полей
        self._car = car

    @property
    def car(self):
        """Метод для получения значения марки машины"""
        return self._car

    def __str__(self):
        return "Instructor({}, age={}, car={})".format(
            self.fio,
            self.age,
            self.car,
        )


class Student(Person):
    """
    Ученик автошколы
    """
    def __init__(self, fio, age, score):
        # Инициализация полей родительского класса
        super(Student, self).__init__(fio, age)
        self._score = None
        # Инициализация собственных полей
        self.score = score

    @property
    def score(self):
        """Метод для получения значения оценки"""
        return self._score

    @score.setter
    def score(self, value):
        """Метод для установки значения оценки"""
        if int(value) < 1 or int(value) > 5:
            raise ValueError("Score value ({}) out of range 1-5".format(value))
        self._score = value

    def __str__(self):
        return "Student({}, age={}, score={})".format(
            self.fio,
            self.age,
            self.score,
        )


class Exam():
    """
    Класс представляющий результаты сдачи воздения
    """
    def __init__(self, instructor, student, date):
        assert isinstance(instructor, Instructor)
        assert isinstance(student, Student)
        self.instructor = instructor
        self.student = student
        self.date = date

    def __str__(self):
        return "Exam({}, {}, date={})".format(
            self.instructor, self.student, self.date
        )
