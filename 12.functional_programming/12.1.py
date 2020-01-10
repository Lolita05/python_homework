#Напишите по 3 примера использования map и filter на произвольных коллекциях -
# отпроцессируйте их элементы и отфильтруйте как вам угодно, для визуализации оберните результат в лист

#map
#1
def division(a):
    return a/2

numbers = (1, 2, 3, 4)
result = map(division, numbers)
print(list(result))

#2
numbers = (1, 2, 3, 4)
result = map(lambda x: x / 2, numbers)
print(list(result))

#3
dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]
result = map(lambda x : x['name'], dict_a)
print(list(result))

#filter
#1
a = [1, 2, 3, 4, 5, 6]
result = filter(lambda x : x % 2 == 0, a)
print(list(result))

#2
dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]
result = filter(lambda x : x['name'] == 'python', dict_a)
print(list(result))

#3
def division(a):
    return a/2
numbers = (1, 2, 3, 4)
result = filter(division, numbers)
print(list(result))
