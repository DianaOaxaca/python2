'''
NAME
	pdb_residues.py
VERSION
	1.0.0
AUTHOR
	Diana H. Oaxaca <hoaxacadiana@gmail.com>
DATE
	26/09/2021
DESCRIPTION
	Programa que a partir de un archivo PDB, nombre de la cadena a analizar y el residuo a buscar, regresa una lista de residuos en la cadena indicada
CATEGORY
	PDB
USAGE
	pdb_residues.py  -i -c -r
ARGUMENTS
	[-i] [input PDB file]
    [-c] [string]
    [-r] [residue]
EXAMPLE
    Comand line:
	    [python3 tareas/pdb_residues.py -i data/1kcw.pdb -c A -r PHE]
    Output:
        [['PHE', 61], ['PHE', 73], ['PHE', 100], ['PHE', 123], ['PHE', 198], ['PHE', 202], ['PHE', 209], ['PHE', 234], ['PHE', 248], ['PHE', 267], ['PHE', 279], ['PHE', 280], ['PHE', 298], ['PHE', 303], ['PHE', 332], ['PHE', 333], ['PHE', 374], ['PHE', 389], ['PHE', 390], ['PHE', 414], ['PHE', 446], ['PHE', 463], ['PHE', 496], ['PHE', 531], ['PHE', 559], ['PHE', 562], ['PHE', 566], ['PHE', 581], ['PHE', 595], ['PHE', 607], ['PHE', 628], ['PHE', 641], ['PHE', 659], ['PHE', 676], ['PHE', 708], ['PHE', 748], ['PHE', 754], ['PHE', 773], ['PHE', 805], ['PHE', 897], ['PHE', 901], ['PHE', 904], ['PHE', 933], ['PHE', 947], ['PHE', 979], ['PHE', 984], ['PHE', 997], ['PHE', 1000], ['PHE', 1010]]
LIBRARIES:
    library argparse
    library Bio
    library PDB
GITHUB LINK
	https://github.com/DianaOaxaca/python2/blob/master/tareas/pdb_residues.py
'''

#Charge libraries
import argparse
from Bio import PDB
#Crear parser and agregar arguments
parser = argparse.ArgumentParser(description= "Este programa busca en un archivo PDB una cadena dada y regresa los residuos indicados por el usuario ")
parser.add_argument('-i', '--input', metavar="ruta al archivo PDB", type=str, help="archivo PDB", required=True)
parser.add_argument('-c','--string', metavar="cadena a analizar",  type=str, help="Cadena", required=True)
parser.add_argument('-r','--residue', metavar="residuo a buscar",  type=str, help="Residuo", required=True)
#Ejecutar metodo parse
arguments = parser.parse_args()
input_file = arguments.input
cadena = arguments.string
residuo = arguments.residue
#Definir funcion para buscar residuo
def get_residue_list(file, chain_name, aminoacid):
    """
    :param file: PDB input file
    :param chain: Input chain to analyze
    :param aminoacid: Input residue to search 
    """
    #Quitar warnings y crear objeto PDB
    parser = PDB.PDBParser(QUIET=True)
    struc = parser.get_structure("prot_1kcw", file)
    #crear lista vacia para anexar residuos
    aa_chain = []
    #Obtener residuos
    for model in struc:
        for chain in model:
            if chain.id == chain_name:
                for residue in chain:
                    if residue.get_resname() == aminoacid:
                        aa_chain.append([residue.get_resname(), residue.get_id()[1]])
    print(aa_chain)
#Llamar a la funcion
get_residue_list(input_file, cadena, residuo)