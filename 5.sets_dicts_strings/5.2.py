#Операции со словарями
items = [(1,2),('s',32)]
dict = dict(items)
del dict[1] #удаляет значение по ключу
print(dict)
#возвращает значение по ключу
for key in dict.keys():
    print(key, '->', dict[key])
new_dict = {} #создание нового словаря
for key, value in dict.items():
    new_dict[value] = key #превращение ключей в элементы в новом словаре
    print(new_dict)
