friends = []
n = int(input())  # задаем количество друзей в списке
for i in range(n):
    friends.append(input())
length = len(friends)
for i in range(length):
    print('Hello, ' + friends[i] + '!') # приветсвуем всех из списка
print('Hello, everyone!')