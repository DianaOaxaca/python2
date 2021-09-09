##importar librerias
#import Bio.Seq
#otra forma de importar modulos Bio=superclase Seq=subclase Seq es una de las subclases de Seq
from Bio.Seq import Seq
from Bio.Seq import MutableSeq
#convertir a string un objeto Seq
seqobj = Seq("TACATCGTG")
print(str(seqobj))
#remplazar un caracter por posicion
mutable = MutableSeq(seqobj)
mutable[0] = "n"
mutable
#Algunas funciones de Seq
print(seqobj.complement())
print(seqobj.reverse_complement())
print(seqobj.translate())
print(seqobj.translate(to_stop = True))
rna = seqobj.transcribe()
rna
print(rna.back_transcribe()) #retrotranscripcion
#Extraer una subsecuencia
print(seqobj[0:3]) #con rango
#o con expresiones regulares
import re
for codon in re.findall(r"(.{3})", str(seqobj)):
    print(codon)
#Buscar un patron con nt_search
from Bio.Seq import Seq
from Bio import SeqUtils
from Bio.SeqUtils import nt_search, GC, molecular_weight
patron = Seq("ACG")
sequence = Seq("ATGCTACGCCGGAATCACGGGAGCTACTGTA")
resultado = nt_search(str(sequence), patron)
print(resultado)
#si queremos el rev compl
resultado = nt_search(str(sequence), patron.reverse_complement())
print(resultado)
print(GC(sequence))
print(molecular_weight(sequence))
##otra libreria para parseos
#SeqIO tiene dos atributos principales id+identificador y seq=secuencia, pero tiene otros adicionales
from Bio import SeqIO
filename = "../../data/seq.nt.fa"
#revisa cada sec records del archivo filename
for seq_record in SeqIO.parse(filename, "fasta"):
    print("ID {}".format(seq_record.id))
    print("len {}".format(len(seq_record)))
    print("Traduccion {}".format(seq_record.seq.translate(to_stop=True)))
    print("Traduccion {}".format(seq_record.seq.translate(to_stop=True, cds=True)))#cds revisa que tenga codon de inicio
#Convertir archivo fasta a diccionario
id_dict = SeqIO.to_dict(SeqIO.parse(filename, "fasta"))
print(id_dict["seq4"].seq.transcribe())
##Ahora con lista
id_list = list(SeqIO.parse(filename, "fasta"))
print(id_list[-1].seq)
#archivos grandes
record_list = SeqIO.index(filename, "fasta")
print(record_list["seq1"])
seq_ids = ["seq2", "seq1"]
with open("../../data/filtrado.fasta", "w") as out_handle:
    for record in SeqIO.parse(filename, "fasta"):
        if record in seq_ids:
            SeqIO.write(record, out_handle, "fasta")
#leer archivo fastq
from Bio import SeqIO
n = 0
for record in SeqIO.parse("../../data/sample.fastq", "fastq"):
    if n < 2:
        print("%s %s" % (record.id, record.seq))
        n += 1
    else:break
print(record.letter_annotations["phred_quality"])          