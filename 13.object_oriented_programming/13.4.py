#Создайте класс для сбора статистик по фастам. Входные параметры:
from Bio import SeqIO
from Bio.SeqUtils import GC
import pylab


class FASTA_stats:
    alphabet = "AUGC"
    molecular_type = "nucleic acid"

    def __init__(self, path):
        self.path = path
        self.records = SeqIO.to_dict(SeqIO.parse(path, "fasta", alphabet=None))

    def __str__(self):
        return self.path

    def SeqCount(self):
        print("Number of sequences from this fasta is", len(self.records))
        print(self.records)

    def HistLength(self):
        lengths = [len(rec) for rec in self.records.values()]
        print("List of sequence lengths:", lengths)
        pylab.hist(lengths, bins=20, color='plum')
        pylab.title("%i sequences\nLengths %i to %i" % (len(lengths), min(lengths), max(lengths)))
        pylab.xlabel("Sequence length (bp)")
        pylab.ylabel("Count")
        pylab.show()

    def GCCount(self):
        GC_values = sorted(GC(rec.seq) for rec in self.records.values())
        print("List of GC content:", GC_values)

    def HistGCCount(self):
        GC_values = sorted(GC(rec.seq) for rec in self.records.values())
        pylab.plot(GC_values, color='c')
        pylab.title("%i sequences\nGC%% %0.1f to %0.1f" % (len(GC_values), min(GC_values), max(GC_values)))
        pylab.xlabel("Genes")
        pylab.ylabel("GC%")
        pylab.show()

    def Hist4mers(self): #still have no idea how to fix dictionary
        for seq_record in self.records.values():
            for i in range(len(seq_record) - 3):
                four_mer_dict = {}
                four_mer = seq_record[i:i + 4]
                score_freq = 0
                a = -1
                while True:
                    a = seq_record.seq.find(str(four_mer.seq), a + 1)
                    if a == -1:
                        four_mer_dict[str(four_mer.seq)] = score_freq
                        break
                    score_freq += 1
                    four_mer_all = {}
                for four_mer_dict in four_mer_dict:
                    four_mer_all.update(four_mer_dict)
                    return four_mer_all
        pylab.hist(four_mer_all.values(), bins=20, color='plum')
        pylab.title("%i sequences\nGC%% %0.1f to %0.1f" % (
        len(four_mer_all.values()), min(four_mer_all.values()), max(four_mer_all.values())))
        pylab.xlabel(four_mer_all.keys())
        pylab.ylabel("")
        pylab.show()

    def DoFastaStats(self):
        print("All FASTA Statistics is present below")
        print("PATH: ", self.__str__())
        print(self.SeqCount())
        print(self.HistLength())
        print(self.GCCount())
        print(self.HistGCCount())
        print(self.Hist4mers())

f = FASTA_stats('/Users/lolitiy/Desktop/1.fasta')
f.SeqCount()
f.GCCount()
f.DoFastaStats()