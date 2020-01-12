import numpy as np
import time
import random
import matplotlib.pyplot as plt

random_time = []
numpy_time = []

for i in range(100):
    t1 = time.time()
    num = np.random.standard_normal(100)
    t2 = time.time()
    numpy_time.append(t2 - t1)
    t1 = time.time()
    temp = []
    for j in range(i):
        num = random.normalvariate(0, 1)
        temp.append(num)
    t2 = time.time()
    random_time.append(t2 - t1)

plt.plot(range(100), random_time, color="red")
plt.plot(range(100), numpy_time, color="blue")
plt.show()