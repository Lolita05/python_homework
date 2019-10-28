#Сконвертируйте список, кортеж, сэт и строку друг в друга всеми возможными способами
# (строка -> лист, строка -> кортеж, ...)

# строка в лист
def Convert(string):
    list = list(string.split(" "))
    return list
s = 'Hello world 124'
print(Convert(s))

# строка в кортеж
str1 = 'Hello world 124'
print(tuple(str1))
#or
s = ['Hello world 124']
print(tuple(s))

# строка в сэт
s = 'Hello world 124'
f = set((s,))

# лист в кортеж
def convert(list):
    return tuple(list)
s = 'Hello world 124'
print(convert(s))

# лист в сэт
l = ['Hello', 'world 124']
print(set(l))

# сэт в строку
s = set(['x','c','v','x','w','g'])
print(', '.join(s)
