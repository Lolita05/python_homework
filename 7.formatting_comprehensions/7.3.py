# Написание comprehension's

#квадраты чисел от 0 до 10
squares = []
for x in range(10):
  squares.append(x ** 2)
print(squares)

#суммы 2-ух чисел взятых из последовательностей от 0 до 3 и от 5 до 8



#переходы из одного нуклеотида в другой (нуклеотиды должны быть разными) - 'A->T'
sequence = ['A', 'T', 'G']


def nucleotide_change(seq):
    for n, i in enumerate(seq):
        if i == 'A':
            seq[n] = 'A -> T', 'A -> G', 'A -> C'
        if i == 'T':
            seq[n] = 'T -> A', 'T -> G', 'T -> C'
        if i == 'G':
            seq[n] = 'G -> A', 'G -> T', 'G -> C'
        if i == 'C':
            seq[n] = 'C -> A', 'C -> G', 'C -> A'
    return seq

print(nucleotide_change(sequence))

#вложенные списки, представляющие матрицу 3 на 3, заполненную от 0 до 9
matrix = [[j for j in range(i-2, i+1)] for i in range(3, 10, 3)]
print(matrix)
