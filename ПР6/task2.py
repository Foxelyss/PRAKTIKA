with open("numsTask2.txt", "r") as file:
    for i in file.read().split():
        print(i, end=" ")