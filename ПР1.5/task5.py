with open("numsTask5.txt", "r") as file:
    numbers = list(map(int, file.read().split()))

min_number_index = numbers.index(min(numbers))
max_number_index = numbers.index(max(numbers))
sum_of_numbers = 0

step = 1 if min_number_index < max_number_index else -1

for i in range(min_number_index + step, max_number_index, step):
    sum_of_numbers += numbers[i]

number_quantity = abs(max_number_index - min_number_index - step)

print(sum_of_numbers / number_quantity)
