# Даны строки S, S1 и S2. Заменить в строке S первое вхождение строки S1 на строку
# S2.

S = input('Строка S: ')

S1 = input('Строка S1: ')

S2 = input('Строка S2: ')

b = len(S1)

k = S.find(S1)

q = (S[0:k+b].replace(S1, S2))

a = q + S[k+b:]

print(a)
