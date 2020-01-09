fh = open("/Users/lolitiy/Desktop/NODE713.fasta")
for line in fh:
    if line.startswith(">"):
        print(line)
fh.close()
