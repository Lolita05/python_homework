#Вычисление среднего
def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)
s = [100, 2, 3, 45, -2, 4]
print(mean(s))
