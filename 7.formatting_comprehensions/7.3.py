# Написание comprehension's

#квадраты чисел от 0 до 10
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = [i**2 for i in l]
print(squares)

#суммы 2-ух чисел взятых из последовательностей от 0 до 3 и от 5 до 8
l = [0, 1, 2, 3]
l1 = [5, 6, 7, 8]
summa = [[i+j] for i in l for j in l1]
print(summa)

#переходы из одного нуклеотида в другой (нуклеотиды должны быть разными) - 'A->T'
sequence = ['A', 'T', 'G', 'C']
sequence = [(f"{i} -> {j}") for i in sequence for j in sequence if i!=j]
print(sequence)

#вложенные списки, представляющие матрицу 3 на 3, заполненную от 0 до 9
matrix = [[j for j in range(i-2, i+1)] for i in range(3, 10, 3)]
print(matrix)
