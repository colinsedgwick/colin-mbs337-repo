# import BaseModel class from pydantic library
from pydantic import BaseModel

# define class ProteinEntry that has parent class BaseModel
class ProteinEntry(BaseModel):
    primaryAccession: str
    organism: dict
    proteinName: str
    sequence: dict
    geneName: str
    function: str

# import json
import json

# read json file and save dictionary from json file into python variable
with open('uniprot_data.json', 'r') as f:
    protein_data = json.load(f)

# create empty list for proteins to be added
proteins = []

# iterate through list of protein dictionaries, turn each dictionary into ProteinEntry object, and append to list
for protein_dict in protein_data['protein_list']:
    proteins.append(ProteinEntry(**protein_dict))

# prints total mass of input list of protein objects
def find_total_mass(list_of_proteins: list[ProteinEntry]) -> None:
    
    # create total mass tracker
    total_mass = 0

    # iterate through each object in list of proteins and add mass to total mass
    for protein in list_of_proteins:
        total_mass += protein.sequence['mass']
    
    # print total mass
    print(total_mass)

# prints list of proteins with mass greater than or equal to 1000 from input list of protein objects
def find_large_proteins(list_of_proteins: list[ProteinEntry]) -> None:
    
    # create empty list of protein names
    protein_names = []
    
    # iterate through each protein in the list, adding the name to the list of names if the 
    # protein mass is greater than or equal to 1000
    for protein in list_of_proteins:
        if protein.sequence['length'] >= 1000:
            protein_names.append(protein.proteinName)
    
    # print protein names list
    print(protein_names)

# prints list of non-Eukaryotic proteins from input list of protein objects
def find_non_eukaryotes(list_of_proteins: list[ProteinEntry]) -> None:
    
    # create empty list of protein names
    protein_names = []

    # iterate through each protein in the input list and add protein name to protein_names list
    # if 'Eukaryota' isn't in the protein's organim's lineage
    for protein in list_of_proteins:
        if 'Eukaryota' not in protein.organism['lineage']:
            protein_names.append(protein.proteinName)

    # print protein names list
    print(protein_names)

# calls each function on the list of ProteinEntry objects
find_total_mass(proteins)
find_large_proteins(proteins)
find_non_eukaryotes(proteins)





