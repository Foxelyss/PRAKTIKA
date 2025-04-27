with open("numsTask1.txt", "r") as file:
    numbers = list(map(int, file.read().split()))

min_number_index = numbers.index(min(numbers))
sum_of_numbers = 1
for i in range(min_number_index + 1, len(numbers)):
    sum_of_numbers *= numbers[i]

print(sum_of_numbers)