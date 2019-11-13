# Сделайте несколько распаковок произвольных списков/кортежей в переменные

#1
def unpack(*args):
    for index, value in enumerate(args):
        print (f'Argument {index}: {value}')

unpack(1, 2, 3, 'noth')
unpack(234, 34, 'what', 'do', 'u', 'mean')

#2
def unpack1(**kwargs):
    for arg, value in kwargs.items():
        print (f'{arg} = {value}')

unpack1(age = 2, name = "Rob")
