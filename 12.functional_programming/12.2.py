#Напишите генератор, осуществляющий считывание фасты и
# возвращающий по 1-ой оттранслированной последовательности

from Bio.Seq import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio.Data import CodonTable

def translate_fasta(path, codon_table = 0):
    if codon_table == 0:
        codon_table = CodonTable.unambiguous_rna_by_name["Standard"]
    genes = SeqIO.parse(path, "fasta")
    for gene in genes:
        gene = Seq(gene, IUPAC.unambiguous_rna)
        yield gene.translate(table=codon_table)

print(list(translate_fasta("ex.fasta")))
