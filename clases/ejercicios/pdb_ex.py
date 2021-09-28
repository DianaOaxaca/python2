#ejercicio1. Crear un objeto structure con el archivo 1kcw.pdb e imprimir el método con el que se creó el modelo y su resolución
from Bio import PDB
parser = PDB.PDBParser(QUIET=True)
struc = parser.get_structure("prot_1kcw", "./data/1kcw.pdb")
struc.header['structure_method']
struc.header['resolution']

#Ejercicio 2. Guardar en una lista todas las cisteinas de la cadena A del archivo 1kcw.pdb
from Bio import PDB
parser = PDB.PDBParser(QUIET=True)
struc = parser.get_structure("prot_1kcw", "./data/1kcw.pdb")
cys_A = []
for model in struc:
    for chain in model:
        if chain.id == 'A':
            for residue in chain:
                if residue.get_resname() == 'CYS':
                    cys_A.append(residue)
cys_A[0]

#Ejercicio 3. Buscar la informacion del atomo S en las cisteinas (elementos y IDs) del primer residuo Cys_A
cys = []
for model in struc:
    for chain in model:
            for residue in chain:
                if residue.get_resname() == 'CYS':
                    cys.append(residue)
                    cys1 = cys[0]
                    for atom in cys1:
                        if atom.element == 'S':
                            print(atom.element, atom.id)

                    #Despues de la linea 27 esto se hizo en clase aunque finalmente es lo mismo que yo hab[ia hecho
                    #print(len(cys))
                    #for atom in cys[0]:
                        #print(atom.element, atom.id)


#SG es nuestro elemento S        

#Ejercicio 4. Calcular la distancia de todos los atomosS patra encontra los que estan cerca
#Calc la dist de los atoms S de las cisteinas de la lista cys_A, guardar los de distancia menor a 8.0 Aæ

cys_A = []
pares =[]
for model in struc:
    for chain in model:
        if chain.id == 'A':
            for residue in chain:
                if residue.get_resname() == 'CYS':
                    cys.append(residue)
                    for atom in cys_A:
                        if atom.element == 'S':
                            for cyst1 in cys_A:
                                for cyst2 in cys_A:
                                    if not (cyst1 == cyst2):
                                        if(cyst1['SG'] - cyst2['SG']) < 8:
                                            # Coordenadas de los átomos
                                            print(cyst1['SG'].coord, cyst2['SG'].coord)
                                            # Pares de ID de los residuos
                                            print(cyst1.id, cyst2.id)
            