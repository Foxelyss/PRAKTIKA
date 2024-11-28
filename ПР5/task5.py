with open("numsTask5.txt", "r") as file:
    numbers = list(map(int, file.read().split()))

min_num_index = numbers.index(min(numbers))
max_num_index = numbers.index(max(numbers))
sum_number = 0

for i in range(min_num_index + 1, max_num_index):
    sum_number += numbers[i]

print(sum_number / (max_num_index - (min_num_index + 1)))