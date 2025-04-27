x, y = float(input()), float(input())
ctg_a = 2 / 5

if -3 <= y <= 2 and abs(x) <= ctg_a * (2 - y):
    print(f"Точка с координатами ({x}, {y}) принадлежит треугольнику")
else:
    print(f"Точка с координатами ({x}, {y}) не принадлежит треугольнику")
