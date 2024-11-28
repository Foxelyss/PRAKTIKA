with open("numsTask3.txt", "r") as file:
    numbers = list(map(int, file.read().split()))

min_num_index = numbers.index(min(numbers))
sum_number = 0

for i in range(min_num_index):
    sum_number += numbers[i]

average_number = sum_number / min_num_index
print(average_number)