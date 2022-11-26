# Task 1 from https://pythonworld.ru/osnovy/tasks.html

def argument(a, b, operation):
    # a, b, operation = map(int, input('Enter two numbers (a, b, and operation):').split())
    if operation == '+':
        print(a + b)
    elif operation == '-':
        print(a - b)
    elif operation == '*':
        print(a * b)
    elif operation == '/':
        print(a / b)
    else:
        print('The symbol is not corrected')
# argument(a, b, operation = map(int, input('Enter two numbers (a, b, and operation):').split()))
argument(3, 4, '/')