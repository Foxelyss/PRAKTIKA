# 1 2 3 4 5 6 7 8 9 10 20 31 55 66 88 89 100

with open("nums.txt", "r") as input_file:
    numbers = list(map(int, input_file.read().split()))

with open("nums.txt", "w") as output_file:
    for i in numbers:
        if i % 2 != 0:
            output_file.write(str(i) + " ")
