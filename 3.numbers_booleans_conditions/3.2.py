# простая формула
x = int(input()) # задаем значение х
y = (2 * x) / 3  # рассчитываем значение y
print(y)

# формула перехода от градусов Цельсия в значение по Фаренгейту
C = int(input()) # задаем значение градусов
F = (9.0 / 5) * C + 32
print (F)

# формула c функцией корня
import math # импорт модуля для работы с математическими формулами
from math import sqrt # импортируем функцию корня
x = float(input())
y = x + sqrt(2 * x - sqrt(x))
print(y)
