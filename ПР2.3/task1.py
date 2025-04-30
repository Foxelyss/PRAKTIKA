# Задание 1. Реализуйте класс Worker, который будет иметь следующие свойства: name,
# surname, rate (ставка за день работы), days (количество отработанных дней). Также класс
# должен иметь метод GetSalary(), который будет выводить зарплату работника. Зарплата -
# это произведение ставки rate на количество отработанных дней days;

class Worker:
    def __init__(self, name: str, surname: str, rate: float, days: int):
        self.name = name
        self.surname = surname
        self.rate = rate
        self.days = days

    def get_salary(self):
        return self.rate * self.days


worker = Worker("Степан", "Смирнов", 5315, 300)

print(f"Работник {worker.name} {worker.surname} со ставкой {worker.rate} рублей проработал {worker.days} дней")
print("И получил ЗП в размере", worker.get_salary(), "рублей")
