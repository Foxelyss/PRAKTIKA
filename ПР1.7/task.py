import json
from datetime import datetime, timedelta


def load_content():
    try:
        with open("notebook.json", 'r') as file:
            return json.load(file)
    except:
        return []


def save_content(content):
    with open("notebook.json", 'w') as file:
        json.dump(content, file, indent=2)


def check_dates_for_completion(content):
    n = 0
    for i in content:
        content[n]["completed"] = check_date_completion(i['date'])
        n += 1
    save_content(content)


def view_task_long(tasks):
    task_number = 1

    for i in tasks:
        print("\nНомер задачи <-", task_number)
        task_number += 1
        print("Статус:", "завершено" if i["completed"] else "в будущем")
        print("Название задачи:", i['name'])
        print("Описание задачи:", i['description'])
        print("Дата окончания задачи:", i['date'])


def get_tasks_by_day(content, day):
    for i in range(len(content)):
        if content[i]['date'] == str(day):
            print(f"{i + 1}. {content[i]['name']} - {content[i]['description']}")


def view_task_short(content):
    print("Список задач")
    for i in range(len(content)):
        print(
            f"{i + 1}. {content[i]['name']} - {content[i]['description']} (до {content[i]['date']})")


def add_task(content):
    name_task = input("Введите название задачи -> ")
    task_description = input("Введите описание задачи -> ")
    task_date = validate_date(input("Введите дату окончанию задачи(YYYY-MM-DD) -> "))
    task = {
        "completed": check_date_completion(task_date),
        "name": name_task,
        "description": task_description,
        'date': task_date
    }
    content.append(task)
    save_content(content)
    print("Задача добавлена")


def delete_task(content):
    view_task_short(content)
    delete_task = int(input("Введите номер задачи для удаления -> ")) - 1

    if 0 <= delete_task < len(content):
        content.pop(delete_task)
        save_content(content)
        print("Задача удалена")
    else:
        print("Неверный номер задачи")


def editing_task(content):
    view_task_short(content)

    task_index = int(input("Введите номер задачи для редактирования -> ")) - 1

    if 0 <= task_index < len(content):
        print("\nДля сохранения оставьте пустым")
        task_name = input("Введите название задачи -> ")
        task_description = input("Введите описание задачи -> ")
        task_date = input("Введите дату окончанию задачи(YYYY-MM-DD) -> ")

        if task_name != "":
            content[task_index]['name'] = task_name
        if task_description != "":
            content[task_index]['description'] = task_description
        if task_date != "":
            content[task_index]['date'] = validate_date(task_date)
            content[task_index]['completed'] = check_date_completion(task_date)

        save_content(content)
        print("Задача отредактирована")
    else:
        print("Неверный номер задачи")


def view_tasks_for_today(content):
    today = datetime.now().date()

    print("Задачи на сегодня:")
    get_tasks_by_day(content, today)


def view_tasks_for_tomorrow(content):
    tomorrow = datetime.now().date() + timedelta(days=1)

    print("Задачи на завтра:")
    get_tasks_by_day(content, tomorrow)


def view_task_for_week(content):
    week_start = datetime.now().date()
    week_end = week_start + timedelta(days=7)
    print("Задачи на неделю")
    for i in range(len(content)):
        data = datetime.strptime(content[i]['date'], "%Y-%m-%d").date()
        if week_start <= data <= week_end:
            print(f"{i + 1}. {content[i]['name']} - {content[i]['description']} (до {content[i]['date']})")


def show_tasks_by_completion(content, completion_state):
    if completion_state:
        print("Выполненные задачи")
    else:
        print("Невыполненные задачи")

    for i in content:
        if i["completed"] == completion_state:
            print(f"{i['name']} - {i['description']} <- дo {i['date']}")


def validate_date(string):
    return str(datetime.strptime(string, "%Y-%m-%d").date())


def check_date_completion(date_to_check):
    date = datetime.strptime(date_to_check, "%Y-%m-%d").date()
    if date < datetime.now().date():
        return True
    return False


check_dates_for_completion(load_content())

while True:
    tasks = load_content()
    print("Действие с файлом:")
    print("1. Добавить задачу")
    print("2. Удалить задачу")
    print("3. Редактировать задачу")
    print("4. Просмотр задач")
    print("5. Просмотр задач на сегодня")
    print("6. Просмотр задач на завтра")
    print("7. Просмотр задач на неделю")
    print("8. Задачи на выполнение")
    print("9. Задачи выполненные")
    print("0. Выход")

    task_number = int(input("Введите номер действия -> "))

    if task_number == 1:
        add_task(tasks)
    elif task_number == 2:
        delete_task(tasks)
    elif task_number == 3:
        editing_task(tasks)
    elif task_number == 4:
        view_task_long(tasks)
    elif task_number == 5:
        view_tasks_for_today(tasks)
    elif task_number == 6:
        view_tasks_for_tomorrow(tasks)
    elif task_number == 7:
        view_task_for_week(tasks)
    elif task_number == 8:
        show_tasks_by_completion(tasks, False)
    elif task_number == 9:
        show_tasks_by_completion(tasks, True)

    if task_number == "0":
        break

    print()
    input("Нажмите enter для продолжения")
