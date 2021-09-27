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


##Sabemos que el objeto gb_record.seq tiene un objeto Secuencia de Biopython, ¿cómo obtengo un subset de esta secuencia del nucléotido 4 al 10?

#Ahora, ¿cómo accedo a la secuencia usando el inicio y el fin del feature cds?¿Cómo obtengo la proteína de este subset usando la secuencia que obtuvimos?

###Ejercicio3 obtener la secuencia, transcripcion y traduccion del gen X

###Ejercicio completo
#Creen una función que a partir del archivo hepatitis.gb imprime: Organismo
#País de la muestra
#Número del aislado
#Nombre del gen y de la proteína que produce (sólo hay un cds)
#Los primeros 15 nucleótidos de ADN. De estos 15 nucleótidos su respectivo ARN y proteína.

#1.- Lee el archivo y crea tu objeto gb_record

#2.- Puedes obtener los primeros datos de annotations (uno de ellos también aparece en features, puedes tomarlo de donde quieras).

#3.- Revisa cómo accedimos en la clase a la información de features.

#4.- Recuerda que la secuencia de gb_record.seq es una secuencia de Bio.Seq y puedes aprovechar sus métodos.

##Ejercicio Imprimir los query_id del archivo multiple_blastoutput.xml cuantos hay?

#Ejercicio imprimir los hit_id del archivo y que sean del query_id Query_73775 Cuantos hay?

#ejercicio Obtener los valores e de los HSP del hit sp |Q3ZAV1.1| del query_id Query_73775 Cual es el mas bajo?


#Ejercicio Usando el archivo test.blastout.xml parsea los resultados 
# e imprime lo siguiente "queryName o query_id, hitID, hit Description o hit_def, 
# e-value" solo si el valor e es menor que 1e-10. (el query name es el query_id y 
# lo encuentran en el blast_record y el Hit Description dentro del alignment.hit_def)
#1.- Hay que recorrer la estructura:
#Primero tenemos el blast_record (la búsqueda de nuestro query y su información están aquí)
#Después tenemos el alineamiento o hit
#Finalmente tenemos cada uno de los HSP con sus estadísticas
#2.- Guarden la información de cada nivel
#3.- Hagan un filtro para solo quedarse con aquellos datos cuyo valor e sea menor a 1e-10