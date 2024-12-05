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


def check_dates(content):
    n = 0
    for i in content:
        data = datetime.strptime(i['data'], "%Y-%m-%d").date()
        if data < datetime.now().date():
            content[n]['status'] = True
        n += 1
    save_content(content)


def view_task_long():
    task_number = 1
    statuses = ["завершено", "в будущем"]

    with open("notebook.json", "r") as file:
        tasks = json.load(file)

    for i in tasks:
        print("\nНомер задачи <-", task_number)
        task_number += 1
        print("Статус:", statuses[int(i['status'])])
        print("Название задачи:", i['name'])
        print("Описание задачи:", i['description'])
        print("Дата окончания задачи:", i['data'])


def filter_data(content, fil_data):
    for i in range(len(content)):
        if content[i]['data'] == str(fil_data):
            print(f"{i + 1}. {content[i]['name'][0]} - {content[i]['description'][1]}")


def view_task_short(content):
    print("Список задач")
    for i in range(len(content)):
        print(
            f"{i + 1}. {content['name'][0]} - {content['description'][1]} (до {content['data']})")


def add_task(content):
    name_task = input("Введите название задачи -> ")
    description_task = input("Введите описание задачи -> ")
    data_task = input("Введите дату окончанию задачи(YYYY-MM-DD) -> ")
    task = {
        "status": False,
        "name":name_task,
        "description": description_task,
        "data": data_task
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

    index_task = int(input("Введите номер задачи для редактирования -> ")) - 1

    if 0 <= index_task < len(content):
        print("\nДля сохранения оставьте пустым")
        task_name = input("Введите название задачи -> ")
        description_task = input("Введите описание задачи -> ")
        data_task = input("Введите дату окончанию задачи(YYYY-MM-DD) -> ")

        if task_name != "":
            content[index_task]['description'] = task_name
        if description_task != "":
            content[index_task]['description'] = description_task
        if data_task != "":
            content[index_task]['data'] = data_task

        save_content(content)
        print("Задача отредактирована")
    else:
        print("Неверный номер задачи")


def view_today(content):
    today = datetime.now().date()
    print("Задачи на сегодня:")
    filter_data(content, today)


def view_task_tomorrow(content):
    tomorrow = datetime.now().date() + timedelta(days=1)
    print(tomorrow)
    print("Задачи на завтра:")
    filter_data(content, tomorrow)


def view_week(content):
    week_start = datetime.now().date()
    week_end = week_start + timedelta(days=7)
    print("Задачи на неделю")
    for i in range(len(content)):
        data = datetime.strptime(content[i]['data'], "%Y-%m-%d").date()
        if week_start <= data <= week_end:
            print(f"{i + 1}. {content[i]['name'][0]} - {content[i]['description'][1]} (до {content[i]['data']})")


def unfulfilled_tasks(content):
    print("Невыполненные задачи")
    for i in content:
        if not i['status']:
            print(f"{i['name'][0]} - {i['description'][1]} <- до {i['data']}")


def completed_tasks(content):
    print("Выполненные задачи")
    for i in content:
        if i['status']:
            print(f"{i['name'][0]} - {i['description'][1]} <- дo {i['data']}")

while True:
    content = load_content()
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

    task_number = input("Введите номер действия -> ")

    if task_number == "1":
        add_task(content)
    elif task_number == "2":
        delete_task(content)
    elif task_number == "3":
        editing_task(content)
    elif task_number == "4":
        view_task_long()
    elif task_number == "5":
        view_today(content)
    elif task_number == "6":
        view_task_tomorrow(content)
    elif task_number == "7":
        view_week(content)
    elif task_number == "8":
        unfulfilled_tasks(content)

    if task_number == "0":
        break

    print()
    input("Нажмите enter для продолжения")