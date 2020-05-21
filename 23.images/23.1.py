#Применить 5 фильтров к своей фотке

import random
from PIL import Image, ImageDraw


# градации серого
def image_grey(image):
    image = Image.open(image)
    draw = ImageDraw.Draw(image) #Создаем инструмент для рисования.
    width = image.size[0] # Ширина
    height = image.size[1] # Высота
    pix = image.load() # Значение пикселей
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            S = (a + b + c) // 3
            draw.point((i, j), (S, S, S))
    del draw
    image.save('AKVPgg5Ahko_grey.jpg')

# негатив
def image_neg(image):
    image = Image.open(image)
    draw = ImageDraw.Draw(image) #Создаем инструмент для рисования.
    width = image.size[0] # Ширина
    height = image.size[1] # Высота
    pix = image.load() # Значение пикселей
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            draw.point((i, j), (255 - a, 255 - b, 255 - c))
    del draw
    image.save('AKVPgg5Ahko_neg.jpg')

def image_bw(image):
    image = Image.open(image)
    draw = ImageDraw.Draw(image) #Создаем инструмент для рисования.
    width = image.size[0] # Ширина
    height = image.size[1] # Высота
    pix = image.load() # Значение пикселей
    factor = int(input('factor:')) # выберите походящий фактор
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            S = a + b + c
            if (S > (((255 + factor) // 2) * 3)):
                a, b, c = 255, 255, 255
            else:
                a, b, c = 0, 0, 0
            draw.point((i, j), (a, b, c))
    del draw
    image.save('AKVPgg5Ahko_bw.jpg')

def image_bright(image):
    image = Image.open(image)
    draw = ImageDraw.Draw(image) #Создаем инструмент для рисования.
    width = image.size[0] # Ширина
    height = image.size[1] # Высота
    pix = image.load() # Значение пикселей
    factor = int(input('factor:'))
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0] + factor
            b = pix[i, j][1] + factor
            c = pix[i, j][2] + factor
            if (a < 0):
                a = 0
            if (b < 0):
                b = 0
            if (c < 0):
                c = 0
            if (a > 255):
                a = 255
            if (b > 255):
                b = 255
            if (c > 255):
                c = 255
            draw.point((i, j), (a, b, c))
    del draw
    image.save('AKVPgg5Ahko_bright.jpg')

# зернистость
def image_noise(image):
    image = Image.open(image)
    draw = ImageDraw.Draw(image) #Создаем инструмент для рисования.
    width = image.size[0] # Ширина
    height = image.size[1] # Высота
    pix = image.load() # Значение пикселей
    factor = int(input('factor:'))
    for i in range(width):
        for j in range(height):
            rand = random.randint(-factor, factor)
            a = pix[i, j][0] + rand
            b = pix[i, j][1] + rand
            c = pix[i, j][2] + rand
            if (a < 0):
                a = 0
            if (b < 0):
                b = 0
            if (c < 0):
                c = 0
            if (a > 255):
                a = 255
            if (b > 255):
                b = 255
            if (c > 255):
                c = 255
            draw.point((i, j), (a, b, c))
    del draw
    image.save('AKVPgg5Ahko_noise.jpg')

def image_purple(image):
    image = Image.open(image)
    draw = ImageDraw.Draw(image) #Создаем инструмент для рисования.
    width = image.size[0] # Ширина
    height = image.size[1] # Высота
    pix = image.load() # Значение пикселей
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            draw.point((i, j), (255, b, 255))
    del draw
    image.save('AKVPgg5Ahko_purple.jpg')

def all_filters(image):
    image_grey(image)
    image_neg(image)
    image_bw(image)
    image_bright(image)
    image_noise(image)
    image_purple(image)


all_filters('AKVPgg5Ahko.jpg')