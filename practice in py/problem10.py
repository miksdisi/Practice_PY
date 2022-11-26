# Task 7 from https://pythonworld.ru/osnovy/tasks.html

day, month, year = map(int, input('Enter three positive numbers (day, month, year):').split())
# print(day, date, month)
if day <= 31 & month <= 12:
    print('Date is correct')
else:
    print('Date is not correct')