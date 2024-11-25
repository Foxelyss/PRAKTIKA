from random import randint

def average_temp(temperature):
    array = []
    for i in range(12):
        array.append(sum(temperature[i])/30)
    return array

temperature = [[randint(0,31) for i in range(30)] for _ in range(12)]
avarages_temperature = sorted(average_temp(temperature))

print(avarages_temperature)
