# Task 8 from https://pythonworld.ru/osnovy/tasks.html

def binary_transformer(x):
    u2 = []
    while True:
        u2.append((x % 2))
        x = (x - (x % 2)) // 2
        if x == 0:
            break
    return u2[::-1]
def decimal_transformer(list_x):
    sum = 0
    for i in range(1, (len(list_x) + 1)):
        if (list_x[-i] == 1):
            sum += (2**(i-1))
    return sum

def XOR_ciper(key, value):
    b = 1
    k = binary_transformer(int(key))
    v = binary_transformer(int(value))
    if len(k) == len(v):
        b = 2
    elif len(k) > len(v):
        for i in range((len(k) - len(v))):
            v.insert(0,0)
    elif len(k) < len(v):
        for i in range((len(v) - len(k))):
            k.insert(0,0)

    XOR = []
    for i in range(1, (len(k)+1)):
        if bool(k[-i]) != bool(v[-i]):
            XOR.insert(0,1)
        else:
            XOR.insert(0,0)

    return XOR

print(decimal_transformer(XOR_ciper(35, 65)))