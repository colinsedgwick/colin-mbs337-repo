# import json and xmltodict libraries
import json
import xmltodict

# open the json file and save dictionary to python variable
with open('uniprot_data.json', 'r') as f:
    protein_data = json.load(f)

# create a new empty dictionary to be the root in the xml file and add protein data dictionary 
# as only entry
root = {}
root['protein_data'] = protein_data

# write the root dictionary to the xml file
with open('proteins.xml', 'w') as o:
    o.write(xmltodict.unparse(root, pretty=True))