# import MMCIFParser class from Bio.PDB.MMCIFParser library
from Bio.PDB.MMCIFParser import MMCIFParser

# create instance of MMCIFParser class
parser = MMCIFParser()

# open mmCIF file for reading and retrieve structure
with open('4HHB.cif', 'r') as f:
    structure = parser.get_structure('hemoglobin', f)

# iterate over models in structure
for model in structure:
    
    # iterate over chains in model
    for chain in model:

        # set residue and atom count to 0
        residue_count = 0
        atom_count = 0

        # iterate over residues in chain
        for residue in chain:

            # set variables equal to 3 tuple values in residue id
            hetfield, resseq, icode = residue.get_id()
            
            # if it is a non-hetero residue, increment residue count 
            # and iterate over atoms in residue and increment atom count
            if hetfield == " ":
                residue_count += 1
                for atom in residue:
                    atom_count += 1
        
        # print the current chain id, non-hetero residue count, and atom count
        print(f"Chain {chain.get_id()}: {residue_count} residues, {atom_count} atoms")