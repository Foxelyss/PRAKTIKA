matrice = []

n = 5

for x in range(n):
    array = []
    for y in range(n):
        array.append(1)
    matrice.append(array)

for x in range(1, n):
    for y in range(1, n):
        matrice[x][y] = matrice[x - 1][y] + matrice[x][y - 1]

for x in matrice:
    print(*x, sep='\t')
