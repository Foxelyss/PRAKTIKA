import random

array = []

for x in range(10):
    array.append(random.randint(-10, 10))

minimal = min(array)
print(array)
print(array.index(minimal))