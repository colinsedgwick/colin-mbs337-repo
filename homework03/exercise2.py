# import csv and json libraries
import csv
import json

# open json file and save dictionary to python variable
with open('uniprot_data.json', 'r') as f:
    protein_data = json.load(f)

# open csv file for writing 
with open('proteins.csv', 'w') as o:
    csv_writer = csv.writer(o)

    # manually create header (list of column names)
    header = ['primaryAccession',
              'proteinName',
              'geneName',
              'organism_scientificName',
              'sequence_length',
              'sequence_mass',
              'function']
    
    # write the header to the first line of csv
    csv_writer.writerow(header)

    # iterates through each protein dictionary and creates a list of values aligned to proper column
    # and then writes this list to the next line in the csv
    for protein in protein_data['protein_list']:
        row = [
            protein['primaryAccession'],
            protein['proteinName'],
            protein['geneName'],
            protein['organism']['scientificName'],
            protein['sequence']['length'],
            protein['sequence']['mass'],
            protein['function']
        ]
        csv_writer.writerow(row)