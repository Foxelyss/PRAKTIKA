# Задание 2.
# Разработайте приложение „I love drink“, со следующим
# функционалом:
# 1) Учет напитков:
# 1.1) Хранение данных об алкогольных напитках и ингредиентах
# 1.2) Учет остатков на складе
# 2) Управление коктейлями:
# 2.1) Хранение данных о коктейлях(название,
# крепость(автоматический расчет исходя из крепости алкогольных
# напитков), состав, цена)
# 3) Операции
# 3.1) Продажа коктейлей и алкогольных напитков
# 3.2) Пополнение запасов
# В приложении должна использоваться база данных для хранения
# информации.

import sqlite3

con = sqlite3.connect("task2.db")

create_table = """
create table if not exists drink(
id integer primary key,
name char(26) not null,
alcohol_percentage float(3) not null
);

create table if not exists ingredient(
id integer primary key,
name char(26) not null
);

create table if not exists cocktails(
id integer primary key,
name char(26) not null,
alcohol_percentage float(2) not null,
price float(2) not null
);

create table if not exists ingredients(
id integer primary key,
cocktail int references cocktails(id),
ingredient int references ingredient(id),
volume float(3) not null
);

create table if not exists drinks(
id integer primary key,
cocktail int references cocktails(id),
drink int references drink(id),
volume float(3) not null
);

create table if not exists supply(
id integer primary key,
supply_date date not null,
ingredient int references ingredient(id),
drink int references drinks(id),
volume float(3) not null,
quantity int not null
);

create table if not exists sells(
id integer primary key,
sell_date date not null,
cocktail int references cocktails(id),
drink int references drinks(id),
volume float(3) not null,
quantity int not null
);
"""

con.executescript(create_table)
con.commit()


def add_drink():
    cursor = con.cursor()
    name = input("Введите название напитка: ")
    alcohol_percentage = int(input("Введите крепкость напитка: ")) / 100

    cursor.execute("insert INTO drink values (null, ?, ?)",
                   (name, alcohol_percentage))

    con.commit()
    print("Напиток добавлен.")


def add_ingredient():
    cursor = con.cursor()

    name = input("Введите название ингредиента: ")

    cursor.execute("insert INTO ingredient values (null, ?)", (name,))

    con.commit()
    print("Ингредиент добавлен.")


def add_cocktail():
    cursor = con.cursor()
    name = input("Введите название коктейля: ")
    price = float(input("Введите цену коктейля: "))

    cursor.execute("insert INTO cocktails values (null, ?, -1, ?)",
                   (name, price))

    con.commit()
    print("Коктейль добавлен.")


def add_drink_to_cocktail():
    cursor = con.cursor()
    cocktail_id = int(input("Введите номер коктейля: "))
    drink_id = int(input("Введите номер напитка: "))
    volume = float(input("Введите объем напитка в коктейле: "))

    cursor.execute("insert INTO drinks values (null, ?, ?, ?)", (cocktail_id, drink_id, volume))

    update_cocktail_alcohol_percentage(cursor.lastrowid)
    print("Напиток добавлен в коктейль.")
    con.commit()


def add_ingredient_to_cocktail():
    cursor = con.cursor()
    cocktail_id = int(input("Введите номер коктейля: "))
    ingredient_id = int(input("Введите номер ингредиента: "))
    volume = float(input("Введите объем ингредиента в коктейле: "))

    cursor.execute("insert INTO ingredients (cocktail, ingredient, volume) values (?, ?, ?)",
                   (cocktail_id, ingredient_id, volume))

    print("Ингредиент добавлен в коктейль.")
    con.commit()

    update_cocktail_alcohol_percentage(cursor.lastrowid)


def update_cocktail_alcohol_percentage(cocktail_id):
    cursor = con.cursor()

    cursor.execute("""
    update cocktails
    set alcohol_percentage = round((
    select sum(drinks.volume * alcohol_percentage) / 
    (select sum(ingredients.volume) + (select sum(drinks.volume) from drinks where cocktail = ?) from ingredients where cocktail = ?) from drinks
    inner join drink on drink.id = drink
    where cocktail = ?
    ), 2)
    where id = ?;
    """, (cocktail_id, cocktail_id, cocktail_id, cocktail_id))

    con.commit()
    print("Крепкость обновлена!")


def sell_drink():
    cursor = con.cursor()
    drink_id = int(input("Введите номер напитка: "))
    quantity = int(input("Введите количество: "))

    cursor.execute("insert INTO sells (sell_date, drink, quantity) values (date(), ?, ?)", (drink_id, quantity))

    con.commit()
    print("Продажа успешна")


def sell_cocktail():
    cursor = con.cursor()
    cocktail_id = int(input("Введите номер коктейля: "))
    quantity = int(input("Введите количество: "))

    cursor.execute("insert INTO sells (sell_date, cocktail, quantity) values (date(), ?, ?)", (cocktail_id, quantity))

    con.commit()
    print("Продажа успешна")


def replenish_ingredient_stock():
    cursor = con.cursor()
    ingredient_id = int(input("Введите ID ингредиента: "))
    quantity = float(input("Введите количество пополнения: "))
    volume = float(input("Введите объем(литры) пополнения: "))
    cursor.execute("insert INTO supply values (null, date(), ?, null, ?, ?)",
                   (ingredient_id, volume, quantity))
    con.commit()
    print("Запас ингредиента пополнен")


def replenish_drink_stock():
    cursor = con.cursor()
    drink_id = int(input("Введите номер напитка: "))
    quantity = float(input("Введите количество пополнения: "))
    volume = float(input("Введите объем(литры) пополнения: "))
    cursor.execute("insert INTO supply values (null, date(), null, ?, ?, ?)", (drink_id, volume, quantity))
    con.commit()
    print("Запас напитка пополнен")


def list_drinks():
    cursor = con.cursor()
    cursor.execute("select * FROM drink")
    drinks = cursor.fetchall()

    print("Список напитков:")
    if not drinks:
        print("Пусто")
        return

    for drink in drinks:
        print(f"№: {drink[0]}; Название: {drink[1]}; Крепость: {drink[2]}; Объем: {drink[3]}")


def list_ingredients():
    cursor = con.cursor()
    cursor.execute("select * FROM ingredient")
    ingredients = cursor.fetchall()

    print("Список ингредиентов:")
    if not ingredients:
        print("Пусто")
        return

    for ingredient in ingredients:
        print(f"ID: {ingredient[0]}, Название: {ingredient[1]}")


def list_cocktails():
    cursor = con.cursor()
    cursor.execute("select * FROM cocktails")
    cocktails = cursor.fetchall()

    print("Список коктейлей:")

    if not cocktails:
        print("Пусто")
        return

    for cocktail in cocktails:
        print(f"№: {cocktail[0]}; Название: {cocktail[1]}; Крепкость: {cocktail[2]}; Цена: {cocktail[3]}")


while True:
    print("Выберите действие:")
    print("1. Добавить напиток")
    print("2. Добавить ингредиент")
    print("3. Добавить коктейль")
    print("4. Добавить напиток в коктейль")
    print("5. Добавить ингредиент в коктейль")
    print("6. Продать напиток")
    print("7. Продать коктейль")
    print("8. Пополнить запас ингредиента")
    print("9. Пополнить запас напитков")
    print("10. Список напитков")
    print("11. Список ингредиентов")
    print("12. Список коктейлей")
    print("13. Выход")

    try:
        choice = int(input("Введите номер действия:"))
    except:
        print("Введите номер!")
        continue

    if choice == 1:
        add_drink()
    elif choice == 2:
        add_ingredient()
    elif choice == 3:
        add_cocktail()
    elif choice == 4:
        add_drink_to_cocktail()
    elif choice == 5:
        add_ingredient_to_cocktail()
    elif choice == 6:
        sell_drink()
    elif choice == 7:
        sell_cocktail()
    elif choice == 8:
        replenish_ingredient_stock()
    elif choice == 9:
        replenish_drink_stock()
    elif choice == 10:
        list_drinks()
    elif choice == 11:
        list_ingredients()
    elif choice == 12:
        list_cocktails()
    elif choice == 13:
        break
    else:
        print("Некорректный ввод.")
        continue

    print()
    input("Нажмите enter для продолжения")
