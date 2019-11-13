# Работа с шаблонами и форматированием строк

#1
drink = ["coffee", "tea", "water"]
food = "cake"


def eat(drink, food):
    return f"Do you want {drink} with {food}?"

a = eat(drink[0], food)
print(a.lower())


#2
grapevines = 17
grapes_in_grapevine = 45


def number_of_grapes(grapevines, grapes_in_grapevine):
    return f"There are total of {grapevines * grapes_in_grapevine} grapes"

print(number_of_grapes(grapevines, grapes_in_grapevine))

#3
x = 3
y = 5


def func(x, y):
    return f"{x} * {y} / 2 = {x * y / 2}"

print(func(x,y))




