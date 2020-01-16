#random walk 1d

import random
import numpy as np
import matplotlib.pyplot as plt

#возможности ходить вверх или вниз
prob = [0.05, 0.95]

#начальная точка
start = 0
positions = [start]

#генерим рандомные точки
rr = np.random.random(1000)
downp = rr < prob[0]
upp = rr > prob[1]

for idownp, iupp in zip(downp, upp):
    down = idownp and positions[-1] > 1
    up = iupp and positions[-1] < 4
    positions.append(positions[-1] - down + up)

plt.plot(positions)
plt.show()

#random walk 2d

import turtle
import random

draw = turtle.Turtle()
draw.speed(10)

for i in range(100):
  draw.forward(10)
  a = random.randrange(0,360,90) #на 90 градусов
  #a = random.randrange(0,200,60) - это красивее
  draw.right(a)