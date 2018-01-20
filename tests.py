"""
Модуль с тестами классов приложения.
Тестируемые классы Person, Instructor, Student
"""
import unittest
# Импортируем тестируемые объекты
from prt.classes import Person, Student, Instructor, Exam

# Импортируем возможные ошибки тестируемыx объектов
from prt.exceptions import ScoreError, ExamPropertyError, ExamDateError

class TestPersonProperties(unittest.TestCase):
    """
    Тестируем класс Person.
    У этого класса должно быть как минимум два поля, fio и age
    Поля должны быть read_only
    """
    fio = "First Last Name"
    age = 10

    def test_read(self):
        """
        Тестируем чтение полей
        """
        person = Person(self.fio, self.age)
        self.assertEqual(person.fio, self.fio)
        self.assertEqual(person.age, self.age)

    def test_write(self):
        """
        Тестируем отсутствие возможности записи полей
        """
        person = Person(self.fio, self.age)

        with self.assertRaises(AttributeError):
            person.fio = "New Name"

        with self.assertRaises(AttributeError):
            person.age = 20


class TestStudent(unittest.TestCase):
    """
    Тестируем класс Student.
    У этого класса должно быть как минимум три поля, fio, age и score
    score должна быть в диапазоне от 1 до 5
    """
    fio = "Student Name"
    age = 20
    score = 5

    def test_score_valid(self):
        """
        Проверяем присутствие поля score, и возможность записи значения в это поле
        """
        student = Student(self.fio, self.age, self.score)
        self.assertEqual(student.score, self.score)
        new_score = 3
        student.score = new_score
        self.assertEqual(student.score, new_score)


    def test_score_invalid(self):
        """
        Проверяем что score принимает только валидные значения
        """
        student = Student(self.fio, self.age, self.score)
        self.assertEqual(student.score, self.score)
        with self.assertRaises(ScoreError):
            student.score = 0

        with self.assertRaises(ScoreError):
            student.score = 6

    def test_is_person(self):
        """
        Класс Student является наследником класса Person
        """
        student = Student(self.fio, self.age, self.score)
        self.assertTrue(isinstance(student, Person), "Студент не наследует класс Person")


class TestInstructor(unittest.TestCase):
    """
    Тестируем класс Student.
    У этого класса должно быть как минимум три поля, fio, age и score
    score должна быть в диапазоне от 1 до 5
    """
    fio = "Instructor Name"
    age = 20
    car = "Car"

    def test_properties(self):
        """
        Проверяем наличие полей fio, age и car
        """
        instructor = Instructor(self.fio, self.age, self.car)
        self.assertEqual(instructor.car, self.car)

    def test_is_person(self):
        """
        Класс Instructor является наследником класса Person
        """
        inst = Instructor(self.fio, self.age, self.car)
        self.assertTrue(isinstance(inst, Person), "Инструктор не наследует класс Person")


class TestExam(unittest.TestCase):
    """
    Класс Exam должен принимать только объекты Instructor и Student
    """
    person = Person("N", 20)
    instructor = Instructor("Inst", 30, "Car")
    student = Student("Name", 20, 5)
    date = "11-11-2011T11:11"

    def test_invalid_properties(self):
        """
        Тестируем, что экзамен принимает только допустимые объекты
        """
        exam = Exam(self.instructor, self.student, self.date)
        self.assertTrue(
            isinstance(exam.instructor, Instructor) and isinstance(exam.student, Student)
        )
        with self.assertRaises(ExamPropertyError):
            Exam(self.person, self.student, self.date)


    def test_invalid_date(self):
        """
        Класс Exam вызывает исключение,
        если получает не правильную дату при инициализации.
        """
        date = "99-99-2011T11:11"
        with self.assertRaises(ExamDateError):
            Exam(self.instructor, self.student, date)

    def test_readonly(self):
        """
        Тестируем отсутствие возможности записи полей
        """
        exam = Exam(self.instructor, self.student, self.date)

        with self.assertRaises(AttributeError):
            exam.instructor = self.instructor

        with self.assertRaises(AttributeError):
            exam.student = self.student


if __name__ == '__main__':
    unittest.main()
