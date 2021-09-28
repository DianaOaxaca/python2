#Einfo, da informacion estandar de las bases de datos la liga aca:
#https://eutils.ncbi.nlm.nih.gov/entrez/eutils/einfo.fcgi
################
   #ACCEDER
################
#ejemplo. Se usa handle.read():
#Cargar librerias
from Bio import Entrez
from pprint import pprint  # para mejor visualización de diccionarios!!
# Correo
Entrez.email = "hoaxaca@ccg.unam.mx"  # IMPORTANTE!!!
# handle con einfo
handle = Entrez.einfo()
result = handle.read() 
handle.close()
#chequemos qué hay en einfo
print(result)
################
#Entrez.read
################
#En el fmt anterior es poco amigable para lectura el parser del modulo Entrez es mas amigable
################
handle = Entrez.einfo()
record = Entrez.read(handle)
# obtenemos diccionario (llave "Dblist")
print(record["DbList"][0:3])  # primeras 3 bases de datos
# cerrar
handle.close()
##############
#  PubMed
##############
handle = Entrez.einfo(db = "pubmed") # indicar db de interes
record = Entrez.read(handle)
handle.close() #cerramos handle
record["DbInfo"]["Description"]  # descripcion de pubmed
### De la misma forma para genome
handle = Entrez.einfo(db="genome")
record = Entrez.read(handle)
record["DbInfo"]["Description"]
print(record["DbInfo"]["FieldList"])
#ver llaves en DbInfo
record["DbInfo"].keys()  # para saber qué podemos consultar
#entrar a la llave LastUpdate
record["DbInfo"]["LastUpdate"]
#buscar en algun field, ver  los campos disponibles en cierta base de datos e imprimir todos sus campos
# imprimir todos los campos a los que podemos accesar de pubmed 
for field in record["DbInfo"]["FieldList"]:
  print("%(Name)s, %(FullName)s, %(Description)s" % field)
#handle.url nos regresa el URL que se ha generado de nuestra petición. Con este URL obtenemos lo que hemos solicitado en nuestro código (request).
#obtener el URL que contiene las busquedas que hemos hecho
print(handle.url)

###################
#     ESEARCH
###################
#sintaxis Entrez.esearch(base de datos a buscar, termino)
#buscar el termino biopython en pubmed, checar cuantos resultados hay
handle = Entrez.esearch(db = "pubmed", term = "biopython")
record = Entrez.read(handle) 
record["Count"]
print(handle.url)
handle.close()
## retmax
#Parametro que indica numero maximo de retrieves

# len(record["IdList"])  #chequemos tamaño 
count = int(record["Count"]) #cambiemos retmax por long de Counts
handle = Entrez.esearch(db="pubmed", term="biopython", retmax=count)
record = Entrez.read(handle) 
handle.close()
len(record["IdList"]) # ahora es de 35!!
record.keys()

#Buscar autores
handle = Entrez.esearch(db="pubmed", term='Valeria Mateo-Estrada',field='AUTH') # o term='Valeria Mateo-Estrada[AUTH]') 
record = Entrez.read(handle)
handle.url  # URL de request
handle.close()
record["IdList"]  # ids de artículos

#buscar varias cosas con operadores booleanos
#Organismo1[Orgn] AND (gen1[Gene] OR gen2[Gene])
#un ejemplo 
termino = "(Aedes[Title] OR Aedes[All Fields])AND((RNA-Seq[Title] OR transcriptomic[Title]) OR (transcriptome[Title] OR sequencing[Title]))"
handle = Entrez.esearch(db="pubmed", term=termino)
result = Entrez.read(handle)
print(result["Count"])  #cuantos encontró
#id list que son 20 default
print(result["IdList"]) # lista de los primero 20 
handle.url  # url de request


