sum = 0
multi = 1


def get_value():
    try:
        return int(input())
    except:
        print("Введите число")
        return get_value()


num = get_value()

quantity = 0
while num != 0:
    sum += num
    multi *= num

    quantity += 1

    num = get_value()

print("Сумма чисел", sum)
print("Умножение чисел", multi)
print("Среднее чисел", sum / quantity)
