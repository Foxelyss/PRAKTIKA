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

candidates = list(map(int, input("Введите числа через пробел: ").split()))
candidates.sort(reverse=True)
target = int(input("Введите цель: "))

combinations = []

for x in range(len(candidates)):
    for t in range(2):
        combination = [candidates[x]]
        number = candidates[x]

        if t % 2 == 0:
            start = len(candidates) - 1
            end = -1 + x
            step = -1
        else:
            start = 0 + x
            end = len(candidates)
            step = 1

        for y in range(start, end, step):
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
