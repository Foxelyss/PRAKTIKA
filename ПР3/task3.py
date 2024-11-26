height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

max_area = 0
for x in range(len(height)):
    for i in range(x + 1, len(height)):

        length = i - x
        min_height = min(height[x], height[i])

        area = min_height * length

        if area > max_area:
            max_area = area

print(max_area)