def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def power(a, b):
    return a ** b

def div(a, b):
    return a / b

def floordiv(a, b):
    return a // b

def mod(a, b):
    return a % b


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

print(f"{a} + {b} = {add(a, b)}")
print(f"{a} - {b} = {sub(a, b)}")
print(f"{a} * {b} = {mul(a, b)}")
print(f"{a} ** {b} = {power(a, b)}")
print(f"{a} / {b} = {div(a, b)}")
print(f"{a} // {b} = {floordiv(a, b)}")
print(f"{a} % {b} = {mod(a, b)}")