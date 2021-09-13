import re
#superclase
class Secuencia:
    #atributo de superclase
    secuencia = True
    #constructor
    def __init__(self, sequence, digitos=0):
        self.sequence = sequence
        self.digitos = digitos
        print(f"Se acaba de crear una secuencia {self.sequence} \n los resultados se redondearan a {self.digitos} digitos")
    #metodo
    def check(dna):
        error = re.findall(r"[^ATGC]", dna)
        try:
            if re.search(r"[^ATGC]", dna):
                raise ValueError("ambiguous base found!")
        except ValueError:
            print("The error caracter is: " + str(error))
    #metodo2
    def nucleotide_content(self, sequence):
        length = len(sequence)
        a_count = sequence.count('A')
        t_count = sequence.count('T')
        at_content = (a_count + t_count)/length
        print("El contenido de AT de tu secuencia es: " + str(round(at_content, self.digitos)))
        g_count = sequence.count('G')
        c_count = sequence.count('C')
        gc_content = (g_count + c_count)/length
        print("El contenido de GC de tu secuencia es: " + str(round(gc_content, self.digitos)))
#Subclase
class GC_Contenido(Secuencia):
    nucleotidos = True
    #Metodo heredado (polimorfismo y overriding)
    def nucleotide_content(self, sequence):
        length = len(sequence)
        g_count = sequence.count('G')
        c_count = sequence.count('C')
        gc_content = (g_count + c_count)/length
        print("El contenido de GC de tu secuencia es: " + str(round(gc_content, self.digitos)))
#subclase2
class AT_Contenido(Secuencia):
    def nucleotide_content(self, sequence):
        length = len(sequence)
        a_count = sequence.count('A')
        t_count = sequence.count('T')
        at_content = (a_count + t_count)/length
        print("El contenido de AT de tu secuencia es: " + str(round(at_content, self.digitos)))
#Escribir datos de secuencia
seq = "CTGCATTATATCGTACGAAATTATCGCGCG"
dig = 4
atributos = Secuencia(seq,dig)
atributos.nucleotide_content(seq)
seq_gc = GC_Contenido(seq, 2)
seq_at = AT_Contenido(seq, 3)
seq_at.nucleotide_content(seq)
seq_gc.nucleotide_content(seq)