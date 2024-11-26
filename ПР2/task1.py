array = []

for x in range(100, 0, -1):
    array.append(x * 3)

for x in range(10):
    for y in range(10):
        print(array[x + y * 10], end=', \t')
    print()
