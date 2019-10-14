# По 5 преобразований  из целых чисел в дробные, из дробных в целые, из каждого из этих типов в строку и наоборот

# из целого в дробное
#1
a = 3
b = float(a)
print(b)

#2
a = int(5 - 3)
b = float(a)
print(b)

#3
a = 21
b = float(a)
print(b)

#4
a = float(2 * 3)
print(a)

#5
a = float(10 / 3)
print(a)

# из дробного в целое
#1
a = int(3  /  5.2)
print(a)

#2
a = 21.25
b = int(a)
print(b)

#3
a = int(2.3 ** 1)
print(a)

#4
a = 59.99
b = int(a)
print(b)

#5
a = int(3.01)
print(a)

# из целого в строку
#1
a = 5
b = str(a)
print(b)

#2
a = str(int(33))
print(a)

#3
a = 55555
b = str(a)
print(b)

#4
a = int(21.2)
b = str(a)
print(b)

#5
a = int(1)
b = str(a)
print(b)

# из дробного в строку
#1
a = float(22.222)
b = str(a)
print(b)

#2
b = str(float(33.1))
print(b)

#3
a = float(15 / 2)
b = str(a)
print(b)

#4
a = float(1.010101)
b = str(a)
print(b)

#5
a = float(15 ** 0.5)
b = str(a)
print(b)

# из строки в целое
#1
a = str(7 - 3)
b = int(a)
print(b)

#2
a = int(str(2 * 2))
print(a)

#3
a = int(str(15))
print(a)

#4
a = int(str(2 / 2))
print(a)

#5
a = str(2345 + 1)
b = int(a)
print(b)

# из строки в дробное
#1
a = float(str(7.4 - 3))
print(a)

#2
a = float(str(7.4 / 3))
print(a)

#3
a = str(4 ** 1.2)
b = float(a)
print(b)

#4
a = str(121212)
b = float(a)
print(b)

#5
a = float(str(2 - 1)) + 1.21
print(a)