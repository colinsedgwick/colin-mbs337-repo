# import json and yaml libraries
import json
import yaml

# open json file and save dictionary to python variable
with open('uniprot_data.json', 'r') as f:
    protein_data = json.load(f)

# write dictionary to yaml file without sorting dictionary keys, and having an explicit start and end to yaml file
with open('proteins.yaml', 'w') as o:
    yaml.dump(protein_data, o, sort_keys=False, explicit_start=True, explicit_end=True)