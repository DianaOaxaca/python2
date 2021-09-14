#Metadata: Información detallada sobre el organismo,
#eferencias a otras bases de datos, publicaciones, etc.
#Features: Características importantes de la secuencia,
#  como secuencias codificantes, proteínas, etc.
#Origin: Secuencia (ADN o proteína). La última línea es un "//" e indican el final del archivo.

##Obtener informacion de un archivo GenBank

from Bio import SeqIO
for gb_record in SeqIO.parse("/Users/diana/Documents/python2/data/aichi.gb", "genbank"):
    print('ID', gb_record.id)
    print('Secuencia', str(gb_record.seq)[0:30],'...') #convertir a cadena de python
    print('Longitud', len(gb_record))

atributos = gb_record.__dict__
atributos.keys()

#GenBank annotations (metadata)
gb_record.annotations

for annotation, value in gb_record.annotations.items():
  print(annotation, value)

###Ejercicio1
#Obtener informacion de las anotaciones, de que organismo viene y la fecha
keys =["date","organism"]
datos = list(map(gb_record.annotations.get, keys)) #map aplica la funcion a todos los elementos de una lista (gb_record.annotations.get -> funcion que extrae el valor correspondiente a una clave) y la lista a plicar la funcion es keys
datos

res = dict((value, gb_record.annotations[value]) for value in ['date', 'organism']
                                                                if value in gb_record.annotations)
res

###Genbank features
for i,feature in enumerate(gb_record.features):
    print("Feature",i+1,'\n',feature)

###Acceder a los valores qualifiers del feature
gb_record.features[0].qualifiers


###Ejercicio2
#Obtener informacion de las anotaciones, numero de aislado y pais de donde proviene
gb_record.features[0].qualifiers['isolation_source']
gb_record.features[0].qualifiers.get("isolate")

###Acceder a los valores location del feature
#dict:atributos unicos
#dir: atributos y metodos unicos y heredados
gb_record.features[1].location

gb_record.features[1].location.__dict__
dir(gb_record.features[1].location)

#Diferencia entre start, end, nofuzzy_start y nofuzzy_end
gb_record.features[1].location.start
gb_record.features[1].location.nofuzzy_start
gb_record.features[1].location.end
gb_record.features[1].location.nofuzzy_end


##Sabemos que el objeto gb_record.seq tiene un objeto Secuencia de Biopython, ¿cómo obtengo un subset de esta secuencia del nucléotido 4 al 10?
gb_record.features
subset = gb_record.seq[3:10]

start = gb_record.features[1].location.nofuzzy_start
end = gb_record.features[1].location.nofuzzy_end
new_seq = gb_record.seq[start+2:end] #para indicar que inicia despues del codon de inicio, esto para la traduccion correcta a proteina
protein = new_seq.translate()

gb_record.features[2].qualifiers#pendiente
