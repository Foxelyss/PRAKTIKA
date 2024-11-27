x, y = float(input()), float(input())
ctg_a = 2 / 5

if -3 <= y <= 2 and abs(x) <= ctg_a * abs(y - 2):
    print("YES")
else:
    print("NO")
