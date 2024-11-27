with open("numsTask4.txt", "r") as file:
    numbers = list(map(int, file.read().split()))

number_quantity = 1
last_num = numbers[0]

for i in range(1, len(numbers)):
    if last_num == numbers[i]:
        number_quantity += 1
    else:
        print(f"Число {last_num} стоит {number_quantity} раза")
        number_quantity = 1

    if i == len(numbers) - 1:
        print(f"Число {last_num} стоит {number_quantity} раза")

    last_num = numbers[i]
