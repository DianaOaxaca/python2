#Acceder al archivo PDB y obtener un objeto Structure
#Primero se crea un objeto PDBParser con un QUIET(evita posibles errores en el archivo, muy comunes)
#Importar librería
from Bio import PDB
parser = PDB.PDBParser(QUIET=True)
#Sintaxis del llamado
struc = parser.get_structure("nombre", "archivo.pdb")
#Formas de vercuantos modelos hay en el objeto structure 
struc.child_dict #diccionario
struc.child_list #lista
#Acceder a metadatos almacenados en el atributo header
struc.header.keys()
struc.header['structure_method']
struc.header['resolution']
#Ejemplo Structure S
from Bio import PDB
parser = PDB.PDBParser(QUIET=True)
struc = parser.get_structure("prot_1fat", "./data/1fat.pdb")
struc.child_dict
print(struc.child_dict) #objeto struct llama al atributo child_dict
struc.child_list #o a child_list
print(struc.child_list)
struc.header.keys() #mostrar elementos
struc.header['structure_method']
struc.header['resolution']
struc.header['source']
struc.header['journal']
#para ver los elementos
for key, value in struc.header.items():
    print(key, value)
# para ver el nombre que asignamos al inicio
print(struc.get_id()) 
#Para obtener el modelo
#acceder por cada elemento
for model in struc:
    print(model)
#acceder como diccionario
model = struc[0] #la llave 0 esta definida por default
print(model)
#accder a los valores como diccionario
model.child_dict
#o como lista
model.child_list
#Acceder a la cadena
for chain in model:
  print(chain)
#individualmente
chain = model['A']
print(chain)
#o asi
chain = model.child_list[0]
#ver la info almacenada
chain.child_list
chain.child_dict
##Acceder al RESIDUO
for residue in chain:
    print(residue)
#como lista
residue = chain[1]
#informacion
residue.get_id()[1] #El id del primer residuo, se encuentra en el segundo elemento
residue.get_resname #obtener el nombre del residuo

#ubicar un residuo que nos interesa

for residue in chain:
    if residue.get_resname() == 'PHE':
        print(residue)
#ver la info almacenada
residue = chain[6] #el elemento6
residue.get_id()[1] #recordar que se indica 1 que es el da id, 0 da otra info como heteroresiduos
residue.get_resname()
#ver elementos
residue.child_list
residue.child_dict
#acceder a un residuo especifico
residuos_int = []
for residue in chain:
    if residue.get_resname() == 'SER':
        residuos_int.append(residue)
print((residuos_int))

#acceder a los atomos
residue = chain[22]
for atom in residue:
    print(atom)
#ver atomo
atom = residue['CA']
type(atom)
atom = residue.child_list[1]
#posicion 3D
atom.coord
#elemento
atom.element
#ID
atom.id
#Se puede ver la distancia en Aæ entre dos atomos tan solo restando
atomo_1 = residue['CA']
atomo_2 = residue['N']
atomo_1 - atomo_2 
atomo_2 - atomo_1


