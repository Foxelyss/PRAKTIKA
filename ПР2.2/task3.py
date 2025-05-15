# Задание 3. Создайте класс с двумя свойствами для хранения целых чисел. Добавить
# метод для вывода на экран и метод для изменения этих чисел. Добавить метод, который
# находит сумму значений этих чисел, и метод который находит наибольшее значение из
# этих чисел. Написать программу, демонстрирующую все возможности класса;

class Pair:
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def set_a(self, a: int):
        self.a = a

    def set_b(self, b: int):
        self.b = b

    def sum(self):
        return self.a + self.b

    def max(self):
        return self.a if self.a > self.b else self.b


pair = Pair(12, 32)

print(f"Максимальное число {pair.max()}, сумма чисел {pair.sum()}")

pair.set_a(42)
print(f"Максимальное число {pair.max()}, сумма чисел {pair.sum()}")

pair.set_b(50)
print(f"Максимальное число {pair.max()}, сумма чисел {pair.sum()}")
