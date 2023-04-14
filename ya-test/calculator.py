def calculate(a, b, method):
    all_methods = '+-*/'
    if method in all_methods:
        if method == '+':
            return sum((a, b))
        elif method == '-':
            return a - b
        elif method == '*':
            return a * b
        elif method == '/':
            return a / b
    else:
        return "Неизвестная операция"

request = input().split()
print(calculate(int(request[0]), int(request[1]), request[2]))