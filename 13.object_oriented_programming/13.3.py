#Напишите класс, унаследовавшись от сэтов, который будет содержать в себе
# только положительные числа при создании и не будет добавлять неположительные элементы

class posNumbersSet(set):
    def __init__(self, *numbers):
        s=[]
        for number in numbers:
            if number > 0:
                s.append(number)
        super().__init__(s)

    def add(self, number):
        if number > 0:
            super().add(number)


a = posNumbersSet(1, 1, 1)
a.add(-2)
a.add(-4)
a.add(4)
