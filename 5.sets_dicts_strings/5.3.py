#Проитерируйтесь по заданному вами словарю и выведите его ключи и элементы
#1
items = [(1,2),('s',32)]
dict1 = dict(items)
values = dict1.values()
keys = dict1.keys()
print(keys, values)

#2
items = [(1,2),('s',32)]
dict1 = dict(items)
for key, value in a_dict1.values():
    print(key, value)

#3
items = [(1,2),('s',32)]
dict1 = dict(items)
for key in dict1.keys():
    print(key, '->', dict1[key])

#4
items = [(1,2),('s',32)]
dict1 = dict(items)
print(dict1.items())

#5
items = [(1,2),('s',32)]
dict1 = dict(items)
for item in dict1.items():
    print(item)
