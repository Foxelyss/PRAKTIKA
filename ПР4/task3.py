with open("numsTask3.txt", "r") as file:
    numbers = list(map(int, file.read().split(",")))

max_nums = 0
min_nums = max(numbers)

for i in numbers:
    if i == 0:
        break
    elif i > max_nums:
        max_nums = i
    elif i < min_nums:
        min_nums = i

print(min_nums/max_nums)