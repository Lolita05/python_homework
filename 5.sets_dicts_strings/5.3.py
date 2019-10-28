#Проитерируйтесь по заданному вами словарю и выведите его ключи и элементы
#1
items = [(1,2),('s',32)]
dict = dict(items)
values = dict.values()
keys = dict.keys()
print(keys, values)

#2
items = [(1,2),('s',32)]
dict = dict(items)
for key, value in a_dict.values():
    print(key, value)

#3
items = [(1,2),('s',32)]
dict = dict(items)
for key in dict.keys():
    print(key, '->', dict[key])

#4
items = [(1,2),('s',32)]
dict = dict(items)
print(dict.items())

#5
items = [(1,2),('s',32)]
dict = dict(items)
for item in dict.items():
    print(item)
