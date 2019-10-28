#Операции со списками
a = set()
b = set()
n = int(input())
for i in range(n):
    a.add(input())
print(a)
for i in range(n):
    b.add(input())
print(b)
a.union(b) #объединение
a.intersection(b) #пересечение
a.difference(b) #вычитание
a.symmetric_difference(b) #симметричное вычитание
a.issubset(b) #проверка на вхождение одного сэта в другой
b.issubset(a) #проверка на вхождение одного сэта в другой
