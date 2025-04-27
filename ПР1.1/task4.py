from random import randint


def generate_array_of_random_int(start, end):
    array = [randint(start, end) for _ in range(10)]
    return array


start, end = int(input()), int(input())
save = generate_array_of_random_int(start, end)

for i in range(10):
    print(f"{i} -> {save[i]}")
