# Магические квадраты издавна интриговали воображение людей:
# дата изготовления древнейшей сохранившейся таблицы относится к 2200 г. до н.э.
# Магический квадрат – это квадратная таблица размера n х n,
# составленная из всех чисел 1, 2, 3 … n2 таким образом,
# что суммы по каждому столбцу, каждой строке и каждой диагонали равны между собой.
# Напишем программу, которая определяет, можно ли считать матрицу магическим квадратом.

# n = int(input('Enter n'))
# matrix = [list(map(int, input().split())) for i in range(n)]
# print(matrix)
# # print(all(i in sum(matrix,[]) for i in range(1, n**2+1)))
# if all(i in sum(matrix,[]) for i in range(1, n**2+1)):
#     print('YES' if all(sum))

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
if all(i in sum(matrix,[]) for i in range(1, n**2 + 1)):
    print('YES' if all(sum(i) == sum(j) == sum([matrix[i][i] for i in range(n)]) == sum([matrix[n-i-1][i] for i in range(n)]) for i in matrix for j in list(map(list, zip(*matrix)))) else 'NO')
else:
    print('NO')