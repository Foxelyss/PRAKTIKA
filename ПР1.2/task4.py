from random import randint


def get_avarage_temperatures(temperature):
    array = []
    for i in range(12):
        array.append(sum(temperature[i]) / 30)
    return array


temperature = []

for _ in range(12):
    month = []
    for i in range(30):
        month.append(randint(0, 31))
    temperature.append(month)

avarage_temperatures = sorted(get_avarage_temperatures(temperature))

print(avarage_temperatures)
