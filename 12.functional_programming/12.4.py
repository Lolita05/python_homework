#Сделайте функцию-генератор, генерирующую все ДНКовые последовательности до длины n

import itertools

def generate(length):
    dna = ['A', 'G', 'C', 'T']
    for seq in range(1, length + 1):
        for item in itertools.product(dna, repeat = seq):
            yield "".join(item)

print(list(generate(2)))
