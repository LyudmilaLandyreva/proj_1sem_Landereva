# С начала суток прошло N секунд (N — целое).
# Найти количество полных минут, прошедших с начала суток.

n = input('Введите количество секунд: ')  # Ввод переменных
while type(n) != int:  # Обработка исключений
    try:
        n = int(n)
    except ValueError:
        print('Введено неверное значение')
        n = input('Введите количество секунд: ')

K = int(n/60)
print(K)
