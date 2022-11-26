# Task 2 from https://pythonworld.ru/osnovy/tasks.html

year = int(input('Enter year:'))
if year % 4 == 0 or (year % 400 == 0 & year % 100 == 0):
    print(year, 'is a leap year')
else:
    print(year, 'is not a leap year')