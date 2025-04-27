strings = []

string = input()
while string != "":
    strings.append(string)
    string = input()

shortest_string = strings[0]
longest_string = strings[0]

for x in strings:
    if len(x) > len(longest_string):
        longest_string = x
    elif len(x) < len(shortest_string):
        shortest_string = x

print('Самый короткий элемент массива: "' + shortest_string + '"')
print('Самый длинный элемент массива: "' + longest_string + '"')
