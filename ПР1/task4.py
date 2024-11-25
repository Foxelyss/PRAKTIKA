from random import randint

def random_num(start, end):
    array = [randint(start, end) for i in range(10)]
    return array

start, end = int(input()), int(input())
save = random_num(start, end)

for i in range(10):
    print(f"{i} -> {save[i]}")