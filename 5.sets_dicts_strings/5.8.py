#Напишите реверскомплементатор (чем больше способов, тем лучше),
# на вход подаётся строка ДНК, нужно чтобы выводился реверскомплемент заглавными буквами
#1
def inversComplement(input):
    output = ''
    for letter in input:
        letter = letter.upper()

        if letter == 'A':
            output += 'T'
        elif letter == 'T':
            output += 'A'
        elif letter == 'G':
            output += 'C'
        else:
            output += 'G'

    return(output[::-1])
s = 'agatacaca'
print(inversComplement(s))

#2
def inversComplement(input):
    return(input.upper().replace('A', 'temp').replace('T', 'A').replace('temp', 'T').replace('G', 'temp').replace('C','G').replace('temp','C')[::-1])
s = 'agatacaca'
print(inversComplement(s))

#3
from Bio.Seq import Seq
s = Seq('agatacaca')
print s.reverse_complement()
