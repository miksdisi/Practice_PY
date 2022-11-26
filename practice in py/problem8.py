# Task 5 from https://pythonworld.ru/osnovy/tasks.html

def sum(a, years):
    for i in range(years):
        a = 1.1 * a
    print(a)
sum(906004, 17)