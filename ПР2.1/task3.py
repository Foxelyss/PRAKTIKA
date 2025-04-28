# Задание 3. Дан целочисленный массив nums, верните true, если какое-либо значение
# встречается в массиве по крайней мере дважды, иначе верните false.
# Ввод: | Вывод:
# nums = [1,2,3,4] false
# nums = [1,1,1,3,3,4,3,2,4,2] true
# nums = [1,2,3,1] true

nums = list(map(int,input("Введите числа через пробел: ").split()))

not_reaccuring = set(nums)

if len(nums) == len(not_reaccuring):
    print("false")
else:
    print("true")