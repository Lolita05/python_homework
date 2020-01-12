#fastq to fasta
def fastq_to_fasta(fastq, fasta, min_length = 50):
    i = 0
    with open(fastq, "r") as fastq:
        with open(fasta, "w") as fasta:
            for line in fastq:
                i += 1
                if i % 4 == 1:
                    title = ">" + line[1:len(line)]
                if i % 4 == 2 and len(line) >= n:
                    fasta.write(title)
                    fasta.write(line)

