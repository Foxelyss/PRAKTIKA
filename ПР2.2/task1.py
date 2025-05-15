# Задание 1. Создайте класс с именем Student, содержащий свойства: фамилия, дата
# рождения, номер группы, успеваемость (массив из пяти элементов). Добавить возможность
# изменения фамилии, даты рождения и номера группы. Добавить возможность вывода
# информации о студенте, фамилия и дата рождения которого введены пользователем.
# Написать программу, демонстрирующую все возможности класса;

from datetime import date


class Student:
    def __init__(self, surname: str, birthdate: date, group_number: int, grades: [int]):
        self.surname = surname
        self.birthdate = birthdate
        self.group_number = group_number

        if len(grades) != 5:
            raise ValueError("Нужен массив из 5 элементов")

        self.grades = grades.copy()

    def set_surname(self, surname: str):
        self.surname = surname

    def set_birthdate(self, birthdate: date):
        self.birthdate = birthdate

    def set_group_number(self, group_number: int):
        self.group_number = group_number

    def print_information(self):
        formatted_date = self.birthdate.strftime("%Y.%m.%d")
        print(f"Студент {self.surname} группы {self.group_number}. {formatted_date} даты рождения")
        print("С оценками", *self.grades)


try:
    uninstantiable_student = Student("Петров", date(2014, 12, 3), 123, [])
except ValueError as a:
    print(a)

student = Student("Сидоров", date(2003, 6, 3), 123, [4, 5, 4, 5, 5])

student.print_information()

student.set_surname("Пирожков")
student.print_information()

student.set_group_number(456)
student.print_information()

student.set_birthdate(date(2007, 12, 12))
student.print_information()
