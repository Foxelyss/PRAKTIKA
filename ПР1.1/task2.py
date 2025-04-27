def get_int_value_from_user():
    try:
        return int(input())
    except:
        print("Введите число")
        return get_int_value_from_user()


number = get_int_value_from_user()

summary = 0
multiplication = 1

quantity = 0

while number != 0:
    summary += number
    multiplication *= number

    quantity += 1

    number = get_int_value_from_user()

avarage_number = summary / quantity

print("Сумма чисел", summary)
print("Умножение чисел", multiplication)
print("Среднее чисел", avarage_number)
