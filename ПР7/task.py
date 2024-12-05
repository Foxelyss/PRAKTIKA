import json
from datetime import datetime, timedelta

def load_content():
    with open("notebook.json", 'r') as file:
        try:
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
    with open("notebook.json", "r") as file:
        tasks = json.load(file)
    for i in tasks:
        print("\nНомер задачи <-", task_number)
        task_number += 1
        print("Статус:", i['status']) #поменять вывод статуса заместо False писать невыполнено, а на True выполнено
        print("Название задачи:", i['name_and_description'][0])
        print("Описание задачи:", i['name_and_description'][1])
        print("Дата окончания задачи:", i['data'])

def filter_data(content, fil_data):
    for i in range(len(content)):
        if content[i]['data'] == str(fil_data):
            print(f"{i+1}. {content[i]['name_and_description'][0]} - {content[i]['name_and_description'][1]}")

def view_task_short(content):
    print("\nСписок задач")
    for i in range(len(content)):
        print(f"{i+1}. {content['name_and_description'][0]} - {content['name_and_description'][1]} (до {content['data']})")

def add_task(content):
    name_task = input("\nВведите название задачи -> ")
    description_task = input("Введите описание задачи -> ")
    data_task = input("Введите дату окончанию задачи(YYYY-MM-DD) -> ")
    task = {
        "status": False,
        "name_and_description": [name_task, description_task],
        "data": data_task
    }
    content.append(task)
    save_content(content)
    print("Задача добавленна")

def delete_task(content):
    view_task_short(content)
    delet_task = int(input("Введите номер задачи для удаления -> ")) - 1
    if 0 <= delet_task < len(content):
        content.pop(delet_task)
        save_content(content)
        print("Задача удалена")
    else:
        print("Неверный номер задачи")

def editing_task(content):
    view_task_short(content)
    index_task = int(input("Введите номер задачи для редактирования -> ")) - 1
    if 0 <= index_task < len(content):
        print("\nДля сохранения оставьте пустым")
        name_task = input("Введите название задачи -> ")
        description_task = input("Введите описание задачи -> ")
        data_task = input("Введите дату окончанию задачи(YYYY-MM-DD) -> ")
        
        if name_task != "":
            content[index_task]['name_and_description'][0] = name_task
        if description_task != "":
            content[index_task]['name_and_description'][1] = description_task
        if data_task != "":
            content[index_task]['data'] = data_task
        
        save_content(content)
        print("Задача отредактирована")
    else:
        print("Неверный номер задачи")

def view_today(content):
    today = datetime.now().date()
    print("\nЗадачи на сегодня:")
    filter_data(content, today)

def view_task_tomorrow(content):
    tomorrow = datetime.now().date() + timedelta(days=1)
    print(tomorrow)
    print("\nЗадачи на завтра:")
    filter_data(content, tomorrow)

def view_week(content):
    week_start = datetime.now().date()
    week_end = week_start + timedelta(days=7)
    print("\nЗадачи на неделю")
    for i in range(len(content)):
        data = datetime.strptime(content[i]['data'], "%Y-%m-%d").date()
        if week_start <= data <= week_end:
            print(f"{i+1}. {content[i]['name_and_description'][0]} - {content[i]['name_and_description'][1]} (до {content[i]['data']})")

def unfulfilled_tasks(content):
    print("\nНевыполненные задачи")
    for i in content:
        if i['status'] == False:
            print(f"{i['name_and_description'][0]} - {i['name_and_description'][1]} <- до {i['data']}")

def completed_tasks(content):
    print("\nВыполненные задачи")
    for i in content:
        if i['status'] == True:
            print(f"{i['name_and_description'][0]} - {i['name_and_description'][1]} <- дo {i['data']}")

# -------main-------
check_dates(load_content())
while True:
    content = load_content()
    print("\nДействие с файлом:")
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

    task_number = input("Выедите номер действия -> ")

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