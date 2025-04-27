with open("numsTask4.txt", "r") as file:
    numbers = list(map(int, file.read().split()))

max_number = max(numbers)

print(numbers.count(max_number - 1))
