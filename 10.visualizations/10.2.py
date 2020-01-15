#Сделаем программу, принимающую путь к fasta, и выводящую распределение длин последовательностей в ней

import matplotlib.pyplot as plt
from Bio import SeqIO


records = list(SeqIO.parse("seqs.fasta", "fasta"))
sizes = [len(rec) for rec in records]
plt.hist(sizes)
plt.xlabel('x')
plt.ylabel('y')
plt.title('seqs')

plt.show()
