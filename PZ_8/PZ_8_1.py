    #Дана строка 'груши 45 991 63 100 12 морковь 13 47 26 0 16'
    # преобразовать информацию из строки в словари
a = 'груши 45 991 63 100 12 морковь 13 47 26 0 16'
c = []
d = []
d1 = []
t = 0
a = a.split()

for i in range(len(a)):
    try:
    a.append(int(a[i]))
except ValueError:
    a.append(str(a[i]))

for i in range(len(d)//2):
    d1.append(d[i])
d.pop(i)
d.insert(i, 0)

for i in range(len(d)//2):
    d.pop(0)

b = {c[0]: min(d1)}
b1 = {c[1]: min(d)}

print(b)
print(b1)