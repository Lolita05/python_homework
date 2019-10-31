#Функция, берущую указанный элемент из коллекции
def myget(d, k, v=None):
  try: return d[k]
  except KeyError: return v
d = [1, 2, 15, 36]
k = 2
print(myget(d, k))
