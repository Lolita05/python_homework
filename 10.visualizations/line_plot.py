#Нарисуем линейный график

import matplotlib.pyplot as plt

x = [1, 10, 13, 33]
y = [3, 7, 12, 40.1]

plt.plot(x, y, color = 'orange')
plt.xlabel('This is x')
plt.ylabel('This is y')
plt.title('X and Y')
plt.show()
