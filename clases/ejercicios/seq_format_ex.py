##ejercicio1
from Bio.Seq import Seq
from Bio import SeqUtils
from Bio.SeqUtils import nt_search, GC, molecular_weight
secuencia2 = Seq("AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG")
orf = Seq("ATG")
orf_posicion = nt_search(str(secuencia2), orf)
for start in range(1,len(orf_posicion)): #1, que no me tome la primer posicion(en donde se encuentra el patron)
    #Se guarda secuencia en posicion de codon de inicio
    sec_prot = secuencia2[start:]
    #Traducir secuencia hasta codon de paro
    proteina = sec_prot.translate(to_stop=True)
    print(proteina)

##Ejercicio 2
#Imprimir codones (separados por un espacio)de cada secuencia en formato fasta
#Usar diccionario, encontrar codones del primer marco de lectura, imprimir en fasta
from Bio import SeqIO
import re
filename = "../../data/seq.nt.fa"
id_dict = SeqIO.to_dict(SeqIO.parse(filename, "fasta"))
for i in id_dict:
    print(">{}".format(i))
    #secuencia a parsear
    sec = id_dict[i].seq
    for codon in re.findall(r".{3}", str(sec[1:len(sec)])):
        print(codon, end="\t")
    print("\n")

#Ejercicio 3
path = "../../data/sample.fastq"
def corte_calidad(path, umbral):
    mala_calidad = []
    for record in SeqIO.parse(path, "fastq"):
        average = sum(record.letter_annotations["phred_quality"]) / len(record.letter_annotations["phred_quality"])
        if (average < umbral):
            temp = (average, record.id)
            mala_calidad.append(temp)
            print("{} secuencias con promedio menor a umbral: {}\n".format(len(mala_calidad), umbral))
corte_calidad(path, 30) 