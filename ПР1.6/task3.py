number = int(input())

if number % 10 == 0 and number % 2 == 0:
    print(f"Число {number} четное и кратно 10")
else:
    print(f"Число {number} не подходит условию")