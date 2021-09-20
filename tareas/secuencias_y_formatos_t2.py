'''
NAME
	secuencias_y_formatos.py
VERSION
	0.0.1
AUTHOR
	Diana H. Oaxaca <hoaxacadiana@gmail.com>
DATE
	20/09/2021
DESCRIPTION
	Programa que a partir de una lista de genes, dada por el usuario, busca organismo, version de secuencia, fuente de aislamiento, pais, secuencia de DNA, RNA y proteina, en un archivo GenBank
CATEGORY
	GenBank
USAGE
	secuencias_y_formatos.py  -i -l
ARGUMENTS
	[-i] [input GenBak file]
    [-l] [list of genes]
EXAMPLE
    Comand line:
	[python3 tareas/secuencias_y_formatos_t2.py -i data/virus.gb -l N P]
    Output:
    Organism:  Isfahan virus
    Sequence version:  1
    Isolate source:  ['Phlebotomus papatasi']
    Country:  ['Iran:Isfahan province']
    Gene name:  ['N']
    The first 15 DNA nucleotides are:  ATGACTTCTGTAGTA
    The first 15 DNA nucleotides are:  AUGACUUCUGUAGUA
    The first 15 DNA nucleotides are:  DFCSKEDCYWLKCVG
    Gene name:  ['P']
    The first 15 DNA nucleotides are:  ATGTCTCGACTCAAC
    The first 15 DNA nucleotides are:  AUGUCUCGACUCAAC
    The first 15 DNA nucleotides are:  VSTQPNFEGLPSVRG
DEPENDENCES
    library argparse
    library Bio
    library SeqIO
GITHUB LINK
	https://github.com/DianaOaxaca/python2/blob/master/tareas/secuencias_y_formatos.py
'''

#Charge libraries
import argparse
from Bio import SeqIO
#Create parser and add arguments
parser = argparse.ArgumentParser(description= "Este programa busca, en un archivo GenBank, caracteristicas especificas de una lista de genes dada por el usuario ")
parser.add_argument("-i", "--input", metavar="path to input GenBank file", type=str, help="GenBank file", required=True)
parser.add_argument('-l','--list', metavar="list of genes to analyze",  nargs="+", help="<Required> Set flag", required=True)
#Execute parse method
arguments = parser.parse_args()
input_file = arguments.input
gene_list = arguments.list
#define features genes function
def resumen(file, genes):
    for gb_record in SeqIO.parse(file, "genbank"):
        print('Organism: ', gb_record.annotations['organism'])
        print('Sequence version: ', gb_record.annotations['sequence_version'])
        print('Isolate source: ', gb_record.features[0].qualifiers['isolation_source'])
        print("Country: ", gb_record.features[0].qualifiers['country'])
        for gene in genes:
            for i,feature in enumerate(gb_record.features):
                feats_number = (i+2) 
                if gb_record.features[feats_number-1].qualifiers['gene']== [gene]:
                    print("Gene name: ", gb_record.features[feats_number-1].qualifiers['gene'])
                    start = gb_record.features[feats_number-1].location.nofuzzy_start
                    end = gb_record.features[feats_number-1].location.nofuzzy_end                    
                    dna = gb_record.seq[start:end]
                    rna = dna.transcribe()
                    dna_prot = gb_record.seq[start+2:end]
                    protein = dna_prot.translate()
                    print("The first 15 DNA nucleotides are: ", dna[0:15])
                    print("The first 15 RNA nucleotides are: ", rna[0:15])
                    print("The first 15 protein amino acids are: ", protein[0:15])
                    break
resumen(input_file, gene_list)