# Задание 5. Создать класс с двумя свойствами. Добавить конструктор с входными
# параметрами. Добавить конструктор, инициализирующий свойства по умолчанию.
# Добавить деструктор, выводящий на экран сообщение об удалении объекта. Написать
# программу, демонстрирующую все возможности класса;

class Pair:
    def __init__(self, a=0 , b=0):
        self.__a = a
        self.__b = b

    def __del__(self):
        print(f"Пара из {self.__a} и {self.__b} удалена!")

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a):
        self.__a = a

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b):
        self.__b = b

first_pair = Pair()
print(f"Пара из {first_pair.a} и {first_pair.b}!")

first_pair.a = 12
print(f"Пара из {first_pair.a} и {first_pair.b}!")

first_pair.b = 321
print(f"Пара из {first_pair.a} и {first_pair.b}!")

second_pair = Pair(12,4)
print(f"Другая пара из {second_pair.a} и {second_pair.b}!")
