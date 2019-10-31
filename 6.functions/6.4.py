#Возвращает список в обратной порядке
def Reverse(lst):
    new_lst = lst[::-1]
    return new_lst


lst = [100, 2, 3, 45, -2, 4]
print(Reverse(lst))
