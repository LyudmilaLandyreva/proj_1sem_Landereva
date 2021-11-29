# Даны целые числа A и B (A < B). Вывести все целые числа от A до B
# включительно; при этом число A должно выводиться 1 раз, число A + 1 должно
# выводиться 2 раза и т. д.

A = input('Введите целое число A: ')  # Ввод переменной
while type(A) != int:  # Обработка исключений
    try:
        A = int(A)
    except ValueError:
        print('Неверный тип данных')
        A = input('Введите целое число A: ')
B = input('Введите целое число B: ')  # Ввод переменной
while type(B) != int:  # Обработка исключений
    try:
        B = int(B)
    except ValueError:
        print('Неверный тип данных')
        B = input('Введите целое число B: ')
while A >= B:
    print('Несоответствует условию')
    A = input('Введите целое число A: ')
    while type(A) != int:  # Обработка исключений
        try:
            A = int(A)
        except ValueError:
            print('Неверный тип данных')
            A = input('Введите целое число A: ')
    B = input('Введите целое число B: ')
    while type(B) != int:  # Обработка исключений
        try:
            B = int(B)
        except ValueError:
            print('Неверный тип данных')
            B = input('Введите целое число B: ')
k = 1
n = 1
i = 1
while A < B:
    while k <= n:
        print(A)
        k += 1
    A += 1
    i += 1
    n = n + i
