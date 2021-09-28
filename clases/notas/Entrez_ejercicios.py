from Bio import Entrez
Entrez.email = "hoaxaca@ccg.unam.mx" 
handle = Entrez.einfo(db="genome")
record = Entrez.read(handle)
record["DbInfo"]["Description"]
print(record["DbInfo"]["FieldList"])
i=-1
for field in record["DbInfo"]["FieldList"]:
    i+= 1
    if field["Name"] == "ORGN":
        print(i, field["Name"], field["Description"])
#acceder a la posici[on 4 que es organismo]
print(record["DbInfor"]["FieldList"][3]["Description"])
