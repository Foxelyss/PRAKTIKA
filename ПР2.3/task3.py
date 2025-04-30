# Задание 3. Создайте класс Calculation, в котором будет одно свойство calculationLine.
# Методы: SetCalculationLine который будет изменять значение свойства,
# SetLastSymbolCalculationLine который будет в конец строки прибавлять символ,
# GetCalculationLine который будет выводить значение свойства, GetLastSymbol получение
# последнего символа, DeleteLastSymbol удаление последнего символа из строки;

class Calculation:
    def __init__(self):
        self.calculation_line = ""

    def set_calculation_line(self, calculation_line: str):
        self.calculation_line = calculation_line

    def set_last_symbol_calculation_line(self, char: str):
        if len(char) != 1:
            raise ValueError("Принимается один символ")

        self.calculation_line += char

    def get_calculation_line(self):
        return self.calculation_line

    def get_last_symbol(self):
        if len(self.calculation_line) == 0:
            return ""

        return self.calculation_line[-1]

    def delete_last_symbol(self):
        self.calculation_line = self.calculation_line[:-1]


my_calculation = Calculation()

print(f"Текущее значение линии: \"{my_calculation.get_calculation_line()}\"")
print(f"Текущее значение последнего элемента: '{my_calculation.get_last_symbol()}'")

my_calculation.set_calculation_line("Степа")

print(f"Текущее значение линии: \"{my_calculation.get_calculation_line()}\"")
print(f"Текущее значение последнего элемента: '{my_calculation.get_last_symbol()}'")

my_calculation.set_last_symbol_calculation_line("н")

print(f"Текущее значение линии: \"{my_calculation.get_calculation_line()}\"")
print(f"Текущее значение последнего элемента: '{my_calculation.get_last_symbol()}'")

my_calculation.delete_last_symbol()
my_calculation.delete_last_symbol()

print(f"Текущее значение линии: \"{my_calculation.get_calculation_line()}\"")
print(f"Текущее значение последнего элемента: '{my_calculation.get_last_symbol()}'")

try:
    my_calculation.set_last_symbol_calculation_line("Символ")
except ValueError as a:
    print(a)
