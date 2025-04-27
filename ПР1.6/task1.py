with open("numsTask1.txt", "r") as file:
    text = file.read().split()

for i in text:
    if len(i) % 2 == 1:
        print(i, end=" ")
