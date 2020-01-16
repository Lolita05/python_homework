import numpy as np
import time
import random
import matplotlib.pyplot as plt


random_time = []
numpy_time = []

for i in range(100): #numpy
    start = time.time()
    numpy_un = np.random.uniform(0, 1, 100)
    done = time.time()
    numpy_time.append(done - start)

    start = time.time() #random
    for j in range(i):
        rand_un = random.uniform(0, 1)
    done = time.time()
    random_time.append(done - start)

plt.plot(range(100), random_time, color="red")
plt.plot(range(100), numpy_time, color="blue")
plt.xlabel('number')
plt.ylabel('time')
plt.legend(["randome", "numpy"])
plt.show()
