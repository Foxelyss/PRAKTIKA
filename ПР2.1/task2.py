# Задание 2. Дан целочисленный массив (candidates) и цель (target), найдите все уникальные
# комбинации чисел, сумма которых равна цели. Каждое число может быть использовано
# только один раз в комбинации. Набор решений не должен содержать повторяющихся
# комбинаций.
# Ввод: Вывод:
# candidates = [2,5,2,1,2]
# target = 5
# [
# [1,2,2],
# [5]
# ]
# candidates = [10,1,2,7,6,1,5]
# target = 8
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]

candidates = list(map(int,input("Введите числа через пробел: ").split()))
target = int(input())

combinations = []

for x in range(len(candidates)):
    combination = [candidates[x]]
    number = candidates[x]

    for y in range(len(candidates)):
        print(number,candidates[y])
        if y != x and (number + candidates[y]) <= target:
            combination.append(candidates[y])
            number += candidates[y]
        elif number >= target:
            break

    combination.sort()

    if number != target:
        continue

    if combination not in combinations:
        combinations.append(combination)

print(combinations)