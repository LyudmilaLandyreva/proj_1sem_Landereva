# Даны целые положительные числа N и K. Используя только операции сложения
# и вычитания, найти частное от деления нацело N на K, а также остаток от этого деления.

N = input('Введите целое число N: ')  # Ввод переменной
while type(N) != int:  # Обработка исключений
    try:
        N = int(N)
    except ValueError:
        print('Неверный тип данных')
        N = input('Введите целое число N: ')
while N < 0:
    print('Неправильно ввели')
    N = input('Введите целое число N: ')
    while type(N) != int:
        try:
            N = int(N)
        except ValueError:
            print('Неправильно ввели')
            N = input('Введите целое число N: ')
K = input('Введите целое число K: ')  # Ввод переменной
while type(K) != int:  # Обработка исключений
    try:
        K = int(K)
    except ValueError:
        print('Неверный тип данных')
        K = input('Введите целое число K: ')
while N < 0:
    print('Неправильно ввели')
    K = input('Введите целое число K: ')
    while type(K) != int:
        try:
            K = int(K)
        except ValueError:
            print('Неправильно ввели')
            K = input('Введите целое число K: ')
s = 0
while N >= K:
    N = N - K
    s += 1
print(s)
print(N)
