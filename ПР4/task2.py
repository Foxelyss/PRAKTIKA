with open("numsTask2.txt", "r") as file:
    numbers = list(map(float, file.read().split(";")))

sum_of_positive_numbers = 0
for x in numbers:
    if x == 0:
        break
    elif x > 0:
        sum_of_positive_numbers += x

print(sum_of_positive_numbers)