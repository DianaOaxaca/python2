import re
#superclase
class Secuencia:
    #atributos
    secuencia = False
    #constructor
    def __init__(self, seq):
        self.seq = seq
        print(f"Se acaba de crear una secuencia {self.seq}")
    #metodo
    def check(dna):
        error = re.findall(r"[^ATGC]", dna)
        try:
            if re.search(r"[^ATGC]", dna):
                raise ValueError("ambiguous base found!")
        except ValueError:
            print("The error caracter is: " + str(error))


seq1 = Secuencia("NCTGCATTATATCGTACGAAATTATCGCGCG")
seq2 = "NCTGCATTATATCGTACGAAATTATCGCGCG"
Secuencia.check(seq2)