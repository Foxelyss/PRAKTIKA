with open("numsTask3.txt", "r") as file:
    numbers = list(map(int, file.read().split(",")))

max_number = numbers[0]
min_number = numbers[0]

for i in numbers:
    if i == 0:
        break
    elif i > max_number:
        max_number = i
    elif i < min_number:
        min_number = i

print("Отношение минимума к максимуму чисел до нуля", min_number / max_number)
