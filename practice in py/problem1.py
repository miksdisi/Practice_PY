# На вход программе подаются два натуральных числа n и m.
# Напишите программу, которая создает матрицу размером n х m,
# заполнив ее по спирали числами от 1 до n x m.
# Спираль начинается в левом верхнем углу и закручивается по часовой стрелке.

n, m = map(int, input('Enter two numbers (n and m):').split()) # map is applies first func to every element the second func;
                                                               # split is destroy input by strings
# print(n, m)
matrix = [[0] * m for i in range(n)] # we are made zero-string n times by m
# print(matrix)
dx, dy, x, y = 0, 1, 0, 0
for i in range(1, n * m + 1):
    matrix[x][y] = i
    if matrix[(x + dx) % n][(y + dy) % m]:
        # print(matrix[(x + dx) % n][(y + dy) % m], i)
        dx, dy = dy, -dx
    x += dx
    y += dy
for line in matrix:
    print(*(f'{i:<5}' for i in line), sep='') # i is equal count of whitespaces; * is using for associate i with
