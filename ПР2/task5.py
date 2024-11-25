from random import randint

months = ["январь", "февраль", "март", "апрель", "май", "июнь",
          "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]


def average_temp(temperature):
    averages = {}
    for i in range(12):
        month = months[i]

        averages[month] = sum(temperature[month]) / 30
    return averages


temperature = {}

for x in range(12):
    month = []

    for i in range(30):
        month.append(randint(0, 31))

    temperature[months[x]] = month

avarages_temperature = average_temp(temperature)

for key, value in avarages_temperature.items():
    print(f"Месяц {key}. Средняя температура: {value}")
