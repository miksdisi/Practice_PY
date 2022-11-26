# Это вариант классической задачи Иосифа Флавия.
# В кругу стоят n человек, пронумерованных числами от 1 до n.
# Начинается расчет, при котором каждый k-й по счету человек выбывает из круга,
# после чего счет продолжается со следующего за ним человека.
# Напишите программу, определяющую номер человека, который останется в кругу последним.

# n, m = map(int, input('Enter two numbers (n and m):').split())
# s = [i for i in range(1, n + 1)]
# while len(s) > 1:
#     for q in range(0, m - 1):
#         s.append(s[q])
#         del s[:m]
# print(s)
# n, m = map(int, input('Enter two numbers (n and m):').split())
# deg = 1
# while n >= deg:
#     if m == 1:
#         deg = 1
#         break
#     else:
#         deg = deg * m
# x = n - deg/m
# print(x)
# # winner = 2 * x + 1
# print(2 % 3)
n, k = int(input()), int(input())
last = 0
for i in range(1, n + 1):
    last = (last + k) % i
    print('i =', i, 'last =', last)
print(last + 1)
n, k = int(input()), int(input())
last = 0
for i in range(1, n + 1):
    last = (last + k) % i
    print('i =', i, 'last =', last)
print(last + 1)
n, k = int(input()), int(input())
last = 0
for i in range(1, n + 1):
    last = (last + k) % i
    print('i =', i, 'last =', last)
print(last + 1)
n, k = int(input()), int(input())
last = 0
for i in range(1, n + 1):
    last = (last + k) % i
    print('i =', i, 'last =', last)
print(last + 1)
n, k = int(input()), int(input())
last = 0
for i in range(1, n + 1):
    last = (last + k) % i
    print('i =', i, 'last =', last)
print(last + 1)
n, k = int(input()), int(input())
last = 0
for i in range(1, n + 1):
    last = (last + k) % i
    print('i =', i, 'last =', last)
print(last + 1)
n, k = int(input()), int(input())
last = 0
for i in range(1, n + 1):
    last = (last + k) % i
    print('i =', i, 'last =', last)
print(last + 1)
