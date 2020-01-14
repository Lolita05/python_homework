#fastq to fasta
from Bio import SeqIO

def fastq_to_fasta(fastq, fasta, min_length = 50):
    fastq = SeqIO.parse(fastq, "fastq")
    fastq = [record for record in fastq if len(record.seq) >= min_length]
    SeqIO.write(fastq, fasta, "fasta")
