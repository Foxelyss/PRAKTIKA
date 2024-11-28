with open("numsTask1.txt", "r") as file:
    numbers = list(map(int, file.read().split()))

min_num_index = numbers.index(min(numbers))
sum_number = 1
for i in range(min_num_index + 1, len(numbers)):
    sum_number *= numbers[i]

print(sum_number)