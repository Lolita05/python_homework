#monkey sort
import random
import numpy as np
import matplotlib.pyplot as plt

#проверка отсортированности списка
def sorted_list(lst):
    #True - отсортирован False - не отсортирован
    if len(lst) < 2:
        return True
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

lst1 = [1, 2, 3]
lst2 = [2, 2, 1, 7]

sorted_list(lst1) #True
sorted_list(lst2) #False

#monkey sort
def monkey_sort(lst):
    while not sorted_list(lst):
        random.shuffle(lst)
    return lst

#monkey sort визуализация
for i in range(2, 10):
    times = []
    for a in range(10):
        l = np.random.randint(0, 50, i)
        start = time.time()
        monkey_sort(l)
        done = time.time()
        times.append((done - start, i))

t = np.array(times, dtype=[("time", "float"), ("length", "float")])
visual = plt.plot(t["length"], t["time"])
plt.xlabel("length")
plt.ylabel("time")
plt.title("Monkey sort time")
plt.show()
