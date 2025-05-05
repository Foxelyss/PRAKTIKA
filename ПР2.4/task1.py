# Задание 1.
# Разработайте приложение по работе со студентами. Приложение
# должно хранить данные о студентах в базе данных. Сущность
# студента должна описываться в виде класса, у которого будут
# следующие поля:
# 1) Имя
# 2) Фамилия
# 3) Отчество
# 4) Группа
# 5) Оценки(массив из 4 элементов)
# В приложении должен быть следующий функционал:
# 1) Добавление нового студента
# 2) Просмотр всех студентов
# 3) Просмотр одного студента, включая его средний балл
# 4) Редактирование студента
# 5) Удаление студента
# 6) Просмотр среднего балла студентов у конкретной группы

import sqlite3

con = sqlite3.connect("task1.db")

create_table = """
create table if not exists student(
id integer primary key,
name char(26) not null,
surname char(26) not null,
lastname char(26) not null,
group_number int not null
);

create table if not exists grades(
id integer primary key,
student_id int references student(id),
grade int not null check(grade between 2 and 5)
);
"""

con.executescript(create_table)
con.commit()


class Student:
    @staticmethod
    def from_result_set(info, grades=None):
        average = None
        if len(info) == 6:
            average = info[5]

        return Student(info[0], info[1], info[2], info[3], info[4], grades, average)

    @staticmethod
    def from_list_result_set_without_grades(lst):
        return list(map(lambda x: Student.from_result_set(x), lst))

    def __init__(self, student_id: int, name: str, surname: str, lastname: str, group: int, grades: [int],
                 average_grade: int):
        self.id = student_id
        self.name = name
        self.surname = surname
        self.lastname = lastname
        self.group = group

        if grades is not None:
            if len(grades) != 4:
                raise ValueError("Оценок должно быть ровно 4!")
                
        self.grades = grades
        self.average = average_grade

    def print_information(self):
        print(f"№: {self.id}, ФИО: {self.name} {self.surname} {self.lastname}, Группа: {self.group}")

        if self.average is not None:
            print("Средний балл:", self.average)
        if self.grades is not None:
            print("Оценки:", *self.grades)


def add_student(student):
    cursor = con.cursor()
    cursor.execute("insert into student values (null, ?, ?, ?, ?)",
                   (student.name, student.surname, student.lastname, student.group))

    student_id = cursor.lastrowid

    ids = [student_id for x in range(len(student.grades))]

    grades_to_insert = zip(ids, student.grades)

    cursor.executemany("insert into grades values (null, ?, ?)", grades_to_insert)
    con.commit()


def view_all():
    cursor = con.cursor()
    cursor.execute("SELECT * FROM student")
    rows = Student.from_list_result_set_without_grades(cursor.fetchall())

    print("\nСписок всех студентов:")
    if len(rows) == 0:
        print("Пусто")
    else:
        for x in rows:
            x.print_information()


def view_student(id):
    cursor = con.cursor()

    cursor.execute("SELECT * FROM student WHERE id=?", (id,))

    student = list(cursor.fetchone())

    if not student:
        print("Студент не найден")
        return

    cursor.execute("SELECT AVG(grade) FROM grades WHERE student_id=?", (id,))
    avg_grade = cursor.fetchone()[0]
    student.append(avg_grade)

    cursor.execute("SELECT grade FROM grades WHERE student_id=?", (id,))
    grades_res = cursor.fetchall()

    grades = tuple(zip(*grades_res))[0]

    student = Student.from_result_set(student, grades)

    print(f"Информация о студенте:")
    student.print_information()


def edit_student(id):
    cursor = con.cursor()

    cursor.execute("SELECT * FROM student WHERE id=?", (id,))
    student = cursor.fetchone()

    if not student:
        print("Студент не найден")
        return

    student = Student.from_result_set(student)

    print("Изменяемый студент")
    student.print_information()

    print("Пропустите значения если не хотите их изменения")

    new_name = input("Новое имя: ")
    new_surname = input("Новая фамилия: ")
    new_lastname = input("Новое отчество: ")
    new_group = input("Новая группа: ")

    if new_name != "":
        cursor.execute("UPDATE student SET name=? WHERE id=?", (new_name, id))
    if new_surname != "":
        cursor.execute("UPDATE student SET surname=? WHERE id=?", (new_surname, id))
    if new_lastname != "":
        cursor.execute("UPDATE student SET lastname=? WHERE id=?", (new_lastname, id))
    if new_group != "":
        cursor.execute("UPDATE student SET group_number=? WHERE id=?", (int(new_group), id))

    print("Применено!")
    con.commit()


def delete_student(id):
    cursor = con.cursor()

    cursor.execute("DELETE FROM student WHERE id=?", (id,))

    if cursor.rowcount != 0:
        print("Удалено!")
    else:
        print("Удалять нечего")
    con.commit()


def group_avg_grade(group_number):
    cursor = con.cursor()
    cursor.execute(
        """
        SELECT student.id, student.name, student.surname, student.lastname, student.group_number, AVG(grade) FROM student 
        inner JOIN grades ON student.id = grades.student_id
        where group_number = ? 
        group by student.id 
        """, (group_number,))

    students_of_group = Student.from_list_result_set_without_grades(cursor.fetchall())

    print("\nСредние оценки в группе:")
    for x in students_of_group:
        x.print_information()


while True:
    print("Меню:")
    print("1. Добавить студента")
    print("2. Вывести всех студентов")
    print("3. Просмотреть информацию о студенте")
    print("4. Редактировать данные студента")
    print("5. Удалить студента")
    print("6. Средние оценки по группам")
    print("0. Выйти из программы")

    choice = int(input("Введите номер действия:"))

    if choice == 1:
        name = input("Имя:")
        surname = input("Фамилия:")
        lastname = input("Отчество:")
        group = int(input("Номер группы:"))
        grades = list(map(int, input("Оценки (через пробел):").split()))

        try:
            student = Student(-1, name, surname, lastname, group, grades, 0)
            add_student(student)
        except ValueError as err:
            print(err)
        except sqlite3.IntegrityError:
            print("Оценки должны быть от 2 до 5")

    elif choice == 2:
        view_all()
    elif choice == 3:
        id = int(input("Номер студента для просмотра:"))

        view_student(id)
    elif choice == 4:
        id = int(input("Номер студента для редактирования:"))

        edit_student(id)
    elif choice == 5:
        id = int(input("Номер студента для удаления:"))

        delete_student(id)
    elif choice == 6:
        group_number = int(input("Введите номер группы: "))

        group_avg_grade(group_number)
    elif choice == 0:
        break
    else:
        print("Неверный выбор")
        continue

    print()
    input("Нажмите enter для продолжения")