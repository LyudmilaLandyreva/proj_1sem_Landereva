# Даны координаты двух различных полей шахматной доски х1, у1, х2, у2 (целые
# числа, лежащие в диапазоне 1-8). Проверить истинность высказывания: «Ладья
# за один ход может перейти с одного поля на другое».

x1 = input('Введите x1: ')  # Ввод переменных
while type(x1) != int:  # Обработка исключений
    try:
        x1 = int(x1)
    except ValueError:
        print('Введен неверный тип данных.')
        x1 = input('Введите x1: ')

    try:
        while (1 > x1) or (8 < x1):  # Ограничение в диапозоне от 1 до 8
            print("Введено неверное число")
            x1 = input("Введите x1: ")
    except TypeError:
        continue

y1 = input('Введите y1: ')  # Ввод переменной
while type(y1) != int:  # Обработка исключений
    try:
        y1 = int(y1)
    except ValueError:
        print('Введен неверный тип данных.')
        y1 = input('Введите y1: ')
    try:
        while (1 > y1) or (8 < y1):  # Ограничение в диапозоне от 1 до 8
            print("Введено неверное число")
            y1 = input("Введите y1: ")
    except TypeError:
        continue

x2 = input('Введите x2: ')  # Ввод переменной
while type(x2) != int:  # Обработка исключений
    try:
        x2 = int(x2)
    except ValueError:
        print('Введен неверный тип данных.')
        x2 = input('Введите x2: ')
    try:
        while (1 > x2) or (8 < x2):  # Ограничение в диапозоне от 1 до 8
            print("Введено неверное число")
            x2 = input("Введите x2: ")
    except TypeError:
        continue

y2 = input('Введите y2: ')  # Ввод переменной
while type(y2) != int:  # Обработка исключений
    try:
        y2 = int(y2)
    except ValueError:
        print('Введен неверный тип данных.')
        y2 = input('Введите y2: ')
    try:
        while (1 > y2) or (8 < y2):  # Ограничение в диапозоне от 1 до 8
            print("Введено неверное число")
            y2 = input("Введите y2: ")
    except TypeError:
        continue

if x1 == x2 or y1 == y2:
    print('Условия задачи выполнены')
else:
    print('Условия задачи не выполнены')
