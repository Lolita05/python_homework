# Написание comprehension's

#квадраты чисел от 0 до 10
a = 0
b = 10


def Squares(a, b):
    for i in range (a, b+1):
        print(i**2)


print(Squares(a, b))

#суммы 2-ух чисел взятых из последовательностей от 0 до 3 и от 5 до 8



#переходы из одного нуклеотида в другой (нуклеотиды должны быть разными) - 'A->T'
sequence = ['A', 'A', 'T', 'G', 'C', 'C']


def nucleotide_change(seq):
    for n, i in enumerate(seq):
        if i == 'A':
            seq[n] = 'T'
        if i == 'T':
            seq[n] = 'A'
        if i == 'G':
            seq[n] = 'C'
        if i == 'C':
            seq[n] = 'G'
    return seq

print(nucleotide_change(sequence))

#вложенные списки, представляющие матрицу 3 на 3, заполненную от 0 до 9
matrix = [[j for j in range(i-2, i+1)] for i in range(3, 10, 3)]
print(matrix)
