#максимальное значение в списке
def maximum(l):
    myMax = l[0]
    for num in l:
        if myMax < num:
            myMax = num
    return myMax
print(maximum([100, 2, 3, 45, -2, 4]))
