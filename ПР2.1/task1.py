# Задание 1. Даны две строки строчных символов: строка J и строка S. Символы, входящие в
# строку J, — «драгоценности», входящие в строку S — «камни». Нужно определить, какое
# количество символов из S одновременно являются «драгоценностями». Проще говоря, нужно
# проверить, какое количество символов из S входит в J.
# Ввод:
# ab
# aabbccd
# Вывод:
# 4

J = input()
S = input()

jewels = 0

for x in S:
    if x in J:
        jewels += 1

print(jewels)