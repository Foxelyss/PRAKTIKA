with open("numsTask4.txt", "r") as file:
    numbers = list(map(int, file.read().split()))

repeating_numbers_quantity = 0
number_not_repeating = True

for i in range(1, len(numbers)):
    if numbers[i - 1] == numbers[i] and number_not_repeating:
        number_not_repeating = False
        repeating_numbers_quantity += 2
    elif numbers[i - 1] == numbers[i]:
        repeating_numbers_quantity += 1
    else:
        number_not_repeating = True

print("Количество одинаковых рядом стоящих чисел:", repeating_numbers_quantity)
