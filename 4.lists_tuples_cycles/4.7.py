# Программа, отбирающая из коллекции чисел только чётные, а затем считающая их сумму

interesting_numbers = (3, 2, 5, 7, 14, 26, 32, 31, 37)
b = []
for i in interesting_numbers:
    if i % 2 == 0:
        b.append(i)
s = sum(b)
print(s)
