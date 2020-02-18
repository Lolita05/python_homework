#Сделайте небольшой класс, описывающий какую-то сущность на ваш выбор
# (организм/тип данных/что-то ещё).
# В классе должен быть конструктор и пара методов



class Ball:

    # Class Attribute
    shape = 'ball'

    # Initializer / Instance Attributes
    def __init__(self, name, weight, color):
        self.name = name
        self.weight = weight
        self.color = color

    # instance method
    def rotation(self, rotate):
        """
        How ball is rotate
        :return:
        """
        return "{} rotate as {} and it is {}".format(self.name, rotate, self.color)

    def weighing(self):
        """
        How ball gets heavier
        :return:
        """
        self.weight +=5

# Instantiate the Ball object
albert = Ball("Albert", 2, "blue")

# call our instance methods
print(albert.rotation("Hot potato"))

albert.weighing()
print("The ball is now weighing", albert.weight)
