with open("input.txt", "r") as input_file:
    lucky_numbers = list(map(int, input_file.readline().split()))
    number_of_participants = int(input_file.readline())
    with open("output.txt", "w+") as output_file:
        for x in range(number_of_participants):
            count = 0
            ticket = list(map(int, input_file.readline().split()))
            for i in lucky_numbers:
                if i in ticket:
                    count += 1
            if count >= 3:
                output_file.write("Lucky\n")
            else:
                output_file.write("Unlucky\n")