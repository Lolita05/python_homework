# Программа, поэлементно складывающая две последовательные коллекции одного размера

list1 = []
n = int(input())
for i in range(n):
   list1.append(input())
list2 = []
n = int(input())
for i in range(n):
   list2.append(input())
list12 = []
for i in range (len(list1)):
    list12.append(int(list1[i])+int(list2[i])) # суммируем элементы из двух списков
print(list12)
