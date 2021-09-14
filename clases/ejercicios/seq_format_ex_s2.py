###Ejercicio1
#Obtener informacion de las anotaciones, de que organismo viene y la fecha
from Bio import SeqIO
for gb_record in SeqIO.parse("/Users/diana/Documents/python2/data/aichi.gb", "genbank"):
    print('ID', gb_record.id)
    print('Secuencia', str(gb_record.seq)[0:30],'...')
    print('Longitud', len(gb_record))

res = dict((value, gb_record.annotations[value]) for value in ['date', 'organism']
                                                                if value in gb_record.annotations)
res

###Ejercicio2
#Obtener informacion de las anotaciones, numero de aislado y pais de donde proviene

res2 = dict((value2, gb_record.features[0].qualifiers[value2]) 
    for value2 in ['country', 'isolate']
        if value2 in gb_record.features[0].qualifiers)
res2