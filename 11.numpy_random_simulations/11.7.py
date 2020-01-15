#Коврик Серпинского

import turtle

def s(n, l):
    if n == 0:
        #рисуем квадратики
        turtle.color('red')
        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(l)
            turtle.left(90)
        turtle.end_fill()

    else:
        #возле центральной точки нарисовать еще 8 маленьких квадратиков
        #создать 2 квадрата на каждой стороне
        #повтортить еще 4 раза
        for _ in range(4):
            #первый квадрат
            s(n - 1, l / 3)
            turtle.forward(l / 3)

            #второй квадрат
            s(n - 1, l / 3)
            turtle.forward(l / 3)

            #переходим на другой угол
            turtle.forward(l / 3)
            turtle.left(90)
     turtle.update()

# для быстроты не обновляем экран
turtle.tracer(0)

# рисуем
s(4, 400)

# закончили рисовать
turtle.done()