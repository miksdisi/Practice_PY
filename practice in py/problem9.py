# Task 6 from https://pythonworld.ru/osnovy/tasks.html

def is_prime(num):
    index = 0
    for i in range(2, num):
        if num % i == 0:
            index += 1
    if index == 0:
        print('Number is prime')
    else:
        print('Number is not prime')
num = int(input('Enter number'))
is_prime(num)