# Task 4 from https://pythonworld.ru/osnovy/tasks.html

month = int(input('enter number of month'))
for i in range(1, 3):
    # if (month == i or month == 12): # so unhappy, it does not work
    if month == i:
        print('it is winter')
for i in range(3, 6):
    if month == i:
        print('it is spring')
for i in range(6, 9):
    if month == i:
        print('it is summer')
for i in range(9, 12):
    if month == i:
        print('it is autumn')
if month == 12:
    print('it is winter')