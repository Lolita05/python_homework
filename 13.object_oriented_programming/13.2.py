#Напишите класс, описывающий РНК
from Bio.Seq import Seq
from Bio.Data import CodonTable
from Bio.Alphabet import IUPAC


class RNA:
    alphabet = "AUGC"
    molecular_type = "nucleic acid"

    def __init__(self, seq, forward=True):
        self.seq = seq
        self.forward = forward
        if not self.forward:
            self.seq = self.seq[::-1]
            self.forward = True

    def translation(self):
        """
        Function to translation of RNA seq into protein seq
        :return: protein seq
        """
        for i in self.seq:
            if i not in "AUGC":
                print("Invalid Input")
                break
            else:
                seq = Seq(self.seq, IUPAC.unambiguous_rna)
                tab = CodonTable.unambiguous_rna_by_name["Standard"]
                if len(seq) % 3 == 0:
                    return seq.translate(table=tab)
                elif (len(seq) + 1) % 3 == 0:
                    return seq.translate(table=tab) + Seq('N')
                elif (len(seq) + 2) % 3 == 0:
                    return seq.translate(table=tab) + Seq('N') + Seq('N')

    def reverse_transcription(self):
        """
        Function to convert rna seq to dna seq
        :return: dna seq
        """
        for i in self.seq:
            if i not in "AUGC":
                print("Invalid Input")
                break
            else:
                dna = self.seq
                dna = dna.translate(dna.maketrans("AUGC", "TACG"))
                return dna


a = RNA('AAAAUGAAGGGUGAAU')
print(a.translation())
print(a.reverse_transcription())
