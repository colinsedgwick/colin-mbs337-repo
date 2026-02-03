import json
import yaml

with open('uniprot_data.json', 'r') as f:
    protein_data = json.load(f)

with open('proteins.yaml', 'w') as o:
    yaml.dump(protein_data, o, sort_keys=False, explicit_start=True, explicit_end=True)