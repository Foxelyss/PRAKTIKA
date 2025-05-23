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

with open('task2.sql', 'r') as file:
    create_table = file.read()

con.executescript(create_table)
con.commit()


def add_drink():
    cursor = con.cursor()
    name = input("Введите название напитка: ")
    alcohol_percentage = int(input("Введите крепкость напитка: ")) / 100
    price = float(input("Цена за литр: "))

    cursor.execute("insert INTO drink values (null, ?, ?, ?)", (name, alcohol_percentage, price))

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


def add_component_to_cocktail(is_ingredient=False):
    cursor = con.cursor()
    cocktail_id = int(input("Введите номер коктейля: "))
    component_id = int(input("Введите номер напитка: "))
    volume = float(input("Введите объем напитка в коктейле: "))

    table = "drink"
    if is_ingredient:
        table = "ingredient"

    cursor.execute(f"insert INTO {table}s values (null, ?, ?, ?)", (cocktail_id, component_id, volume))

    update_cocktail_alcohol_percentage(cursor.lastrowid)
    print("Напиток добавлен в коктейль.")
    con.commit()


def remove_component_from_cocktail(is_ingredient=False):
    cursor = con.cursor()
    cocktail_id = int(input("Введите номер коктейля: "))
    component_id = int(input("Введите номер компонента: "))

    table = "drink"
    if is_ingredient:
        table = "ingredient"

    cursor.execute(f"delete from {table}s where cocktail=? and {table}=?",
                   (cocktail_id, component_id))

    print("Компонент удалён из коктейля.")
    con.commit()

    update_cocktail_alcohol_percentage(cursor.lastrowid)


def update_cocktail_alcohol_percentage(cocktail_id):
    cursor = con.cursor()

    cursor.execute("""
    update cocktails
    set alcohol_percentage = round((
    select COALESCE(sum(drinks.volume * alcohol_percentage),0) / 
    (select COALESCE(sum(ingredients.volume), 0) + (select COALESCE(sum(drinks.volume), 0) from drinks where cocktail = ?) 
    from ingredients where cocktail = ?) from drinks
    inner join drink on drink.id = drink
    where cocktail = ?
    ), 2)
    where id = ?;
    """, (cocktail_id, cocktail_id, cocktail_id, cocktail_id))

    con.commit()
    print("Крепкость обновлена!")


def sell_drink_or_cocktail(is_cocktail=False):
    cursor = con.cursor()
    drink_id = int(input("Введите номер: "))
    quantity = int(input("Введите количество: "))
    volume = float(input("Введите количество: "))
    price = float(input("Введите сумму закупки: "))

    table = "drink"
    if is_cocktail:
        table = "cocktail"

    cursor.execute(f"insert INTO sells_{table} values (null, date(), ?, ?, ?, ?)",
                   (drink_id, volume, quantity, price))

    con.commit()
    print("Продажа успешна")


def replenish_component_stock(is_ingredient=False):
    cursor = con.cursor()
    ingredient_id = int(input("Введите ID ингредиента: "))
    quantity = int(input("Введите количество пополнения: "))
    volume = float(input("Введите объем(литры) пополнения: "))
    price = float(input("Введите сумму закупки: "))

    table = "drink"
    if is_ingredient:
        table = "ingredient"

    cursor.execute(f"insert INTO supply_{table} values (null, date(), ?, ?, ?, ?)",
                   (ingredient_id, volume, quantity, price))
    con.commit()
    print("Запас ингредиента пополнен")


def list_drinks():
    cursor = con.cursor()
    cursor.execute("select * FROM drink")
    drinks = cursor.fetchall()

    print("Список напитков:")
    if not drinks:
        print("Пусто")
        return

    for drink in drinks:
        print(f"№: {drink[0]}; Название: {drink[1]}; Крепость: {drink[2]}; Цена за литр: {drink[3]}")


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

        volume = 0

        print("Ингредиенты в составе:")

        ingredients = cursor.execute("""
        select ingredient.name, volume from ingredients
        inner join ingredient on ingredient.id = ingredient
        where ingredients.cocktail = ?
        """, (cocktail[0],)).fetchall()

        if not ingredients:
            print("Пусто")
        else:
            for x in ingredients:
                print(f"{x[0]} в объёме {x[1]}")
                volume += x[1]

        print("\nНапитки в составе:")

        drinks = cursor.execute("""
        select drink.name , alcohol_percentage, volume FROM drinks
        inner join drink on drinks.drink = drink.id
        where drinks.cocktail = ?
        """, (cocktail[0],)).fetchall()

        if not drinks:
            print("Пусто")
        else:
            for x in drinks:
                print(f"{x[0]} в объёме {x[1]}")
                volume += x[1]

        print("\nПолный объём:", volume)

def list_sells():
    cursor = con.cursor()
    cursor.execute("""
    select sells_drink.id, sell_date, name, volume, quantity, price from sells_drink
    inner join drink on sells_drink.drink = drink.id
    """)
    drinks_sells = cursor.fetchall()

    print("Продажи напитков")
    if not drinks_sells:
        print("Пусто")
    else:
        for x in drinks_sells:
            print(f"№{x[0]} Дата: {x[1]}, {x[2]} в объеме {x[3]} литр {x[4]} шт. на сумму {x[5]} рублей")

    cursor.execute("""
        select sells_cocktail.id, sell_date, name, volume, quantity, sells_cocktail.price from sells_cocktail
        inner join cocktails on sells_cocktail.cocktail = cocktails.id
        """)
    cocktails_sells = cursor.fetchall()

    print("Продажи коктейлей")
    if not cocktails_sells:
        print("Пусто")
    else:
        for x in cocktails_sells:
            print(f"№{x[0]} Дата: {x[1]}, {x[2]} в объеме {x[3]} литр {x[4]} шт. на сумму {x[5]} рублей")


def list_replenishment():
    cursor = con.cursor()
    cursor.execute("""
            select supply_drink.id, supply_date, name, volume, quantity, price from supply_drink
            inner join drink on supply_drink.drink = drink.id
            """)
    drinks_supply = cursor.fetchall()

    print("Пополнение напитков")
    if not drinks_supply:
        print("Пусто")
    else:
        for x in drinks_supply:
            print(f"№{x[0]} Дата: {x[1]}, {x[2]} в объеме {x[3]} литр {x[4]} шт. на сумму {x[5]} рублей")

    cursor.execute("""
            select supply_ingredient.id, supply_date, name, volume, quantity, price from supply_ingredient
            inner join ingredient on supply_ingredient.ingredient = ingredient.id
            """)
    ingredient_supply = cursor.fetchall()

    print("Продажи коктейлей")
    if not drinks_supply:
        print("Пусто")
    else:
        for x in ingredient_supply:
            print(f"№{x[0]} Дата: {x[1]}, {x[2]} в объеме {x[3]} литр {x[4]} шт. на сумму {x[5]} рублей")

while True:
    print("Выберите действие:")
    print("1. Добавить напиток")
    print("2. Добавить ингредиент")
    print("3. Добавить коктейль")
    print("4. Добавить напиток в коктейль")
    print("5. Добавить ингредиент в коктейль")
    print("6. Убрать напиток из коктейля")
    print("7. Убрать ингредиент из коктейля")
    print("8. Продать напиток")
    print("9. Продать коктейль")
    print("10. Пополнить запас ингредиента")
    print("11. Пополнить запас напитков")
    print("12. Посмотреть продажи")
    print("13. Посмотреть пополнения")
    print("14. Список напитков")
    print("15. Список ингредиентов")
    print("16. Список коктейлей")
    print("17. Выход")

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
        add_component_to_cocktail()
    elif choice == 5:
        add_component_to_cocktail(True)
    elif choice == 6:
        remove_component_from_cocktail()
    elif choice == 7:
        remove_component_from_cocktail(True)
    elif choice == 8:
        sell_drink_or_cocktail()
    elif choice == 9:
        sell_drink_or_cocktail(True)
    elif choice == 10:
        replenish_component_stock()
    elif choice == 11:
        replenish_component_stock(True)
    elif choice == 12:
        list_sells()
    elif choice == 13:
        list_replenishment()
    elif choice == 14:
        list_drinks()
    elif choice == 15:
        list_ingredients()
    elif choice == 16:
        list_cocktails()
    elif choice == 17:
        break
    else:
        print("Некорректный ввод.")
        continue

    print()
    input("Нажмите enter для продолжения")
