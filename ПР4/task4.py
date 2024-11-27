with open("numsTask4.txt", "r") as file:
    numbers = list(map(int, file.read().split()))

repeating_numbers_quantity = 0
number_quantity = 1
last_num = numbers[0]

for i in range(1, len(numbers)):
    if last_num == numbers[i]:
        number_quantity += 1
    elif number_quantity != 1:
        repeating_numbers_quantity += number_quantity
        number_quantity = 1

    if i == len(numbers) - 1:
        repeating_numbers_quantity += number_quantity

    last_num = numbers[i]

print("Количество одинаковых рядом стоящих чисел:",repeating_numbers_quantity)