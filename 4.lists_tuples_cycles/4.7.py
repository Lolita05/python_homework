# Программа, отбирающая из коллекции чисел только чётные, а затем считающая их сумму

interesting_numbers = (3, 2, 5, 7, 14, 26, 32, 31, 37)
i_n = list(interesting_numbers)
b = []
for i in i_n:
    if i % 2 == 0:
        b.append(i)
b = tuple(b)
s = sum(b)
print(s)
