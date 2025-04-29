# Задание 2. Создайте класс с именем Train, содержащий свойства: название пункта
# назначения, номер поезда, время отправления. Добавить возможность вывода
# информации о поезде, номер которого введен пользователем. Написать программу,
# демонстрирующую все возможности класса;

from datetime import datetime


class Train:
    def __init__(self, arrival_point_name: str, train_number: int, departure_time: datetime):
        self.arrival_point_name = arrival_point_name
        self.train_number = train_number
        self.departure_time = departure_time

    def print_information(self):
        formatted_date = self.departure_time.strftime("%d %b %Y %H:%M:%S")
        print(f"Поезд отправляется в: {self.arrival_point_name} с номером {self.train_number} на время {formatted_date}")


trains = [
    Train("Магадан", 130, datetime(2024, 12, 2, 12, 51)),
    Train("Томск", 240, datetime(2024, 2, 2, 19, 12)),
    Train("Москва", 30, datetime(2012, 6, 2, 1, 1))
]


def find_train_by_id(train_number):
    for x in trains:
        if x.train_number == train_number:
            x.print_information()
            return


find_train_by_id(130)
find_train_by_id(240)
