#Вычисление среднего

s = [100, 2, 3, 45, -2, 4]


from functools import reduce
from operator import truediv

def mean(numbers):
    return truediv(*reduce(lambda a, b: (a[0] + b[1], b[0]),
                           enumerate(numbers, start=1),
                           (0, 0)))

print(mean(s))