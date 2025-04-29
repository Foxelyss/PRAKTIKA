# Задание 4. Описать класс, реализующий счетчик, который может увеличивать или
# уменьшать свое значение на единицу. Предусмотреть инициализацию счетчика со
# значением по умолчанию и произвольным значением. Счетчик имеет два метода:
# увеличения и уменьшения, — и свойство, позволяющее получить его текущее состояние.
# Написать программу, демонстрирующую все возможности класса;

class Counter:
    def __init__(self, counter_start_value=0):
        self.__counter = counter_start_value

    def increment(self):
        self.__counter += 1

    def decrement(self):
        self.__counter -= 1

    @property
    def counter(self):
        return self.__counter


my_task_counter = Counter(3)
print("Значение счётчика: ", my_task_counter.counter)

my_task_counter.increment()
print("Значение счётчика: ", my_task_counter.counter)

my_task_counter.increment()
print("Значение счётчика: ", my_task_counter.counter)

my_task_counter.decrement()
print("Значение счётчика: ", my_task_counter.counter)

my_task_counter.decrement()
print("Значение счётчика: ", my_task_counter.counter)

test_counter = Counter()
print("Значение другого счётчика: ", test_counter.counter)
