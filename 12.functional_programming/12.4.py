#Сделайте функцию-генератор, генерирующую все ДНКовые последовательности до длины n

import itertools

def generate(length):
    dna = ['A', 'G', 'C', 'T']
    for item in itertools.product(dna, repeat = length):
        yield "".join(item)

print(list(generate(2)))
