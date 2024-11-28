with open("numsTask4.txt", "r") as file:
    numbers = list(map(int, file.read().split()))

max_num_index = max(numbers)

print(numbers.count(max_num_index-1))
