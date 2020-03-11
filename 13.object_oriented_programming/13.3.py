#Напишите класс, унаследовавшись от сэтов, который будет содержать в себе
# только положительные числа при создании и не будет добавлять неположительные элементы

class posNumbersSet(set):
    def __init__(self, numbers):
        s=[]
        for number in numbers:
            if number <= 0:
                continue
            else:
                s.append(number)
        super().__init__(s)


    def pos(self):
        return abs(s)


a = posNumbersSet([1, -2, 1, 1])
a.pos()





