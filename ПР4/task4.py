with open("numsTask4.txt", "r") as file:
    numbers = list(map(int, file.read().split()))

numbers_quantity = set(numbers)
nums = 1
last_num = numbers[0]

for i in range(1,len(numbers)):
    if last_num == numbers[i]:
        nums += 1
    else:
        print(f"Число {last_num} стоит {nums} раза")
        nums = 1

    if i == len(numbers) - 1:
        print(f"Число {last_num} стоит {nums} раза")

    last_num = numbers[i]

