from random import uniform, randint

array = []

for x in range(randint(6, 10)):
    array.append(uniform(-20,20))

print("Изначальный массив:")
print(*array)

positive_values_of_array = []
negative_values_of_array = []

for x in array:
    if x > 0:
        positive_values_of_array.append(x)
    if x < 0:
        negative_values_of_array.append(x)

print("Положительные числа из массива:")
print(*positive_values_of_array)
print("Отрицательные числа из массива:")
print(*negative_values_of_array)
