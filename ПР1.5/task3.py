with open("numsTask3.txt", "r") as file:
    numbers = list(map(int, file.read().split()))

min_number_index = numbers.index(min(numbers))
sum_of_numbers = 0

for i in range(min_number_index):
    sum_of_numbers += numbers[i]

average_number = sum_of_numbers / min_number_index
print(average_number)
