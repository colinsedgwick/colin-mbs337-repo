# import SimpleFastaParser class from Bio.SeqIO.FastaIO library
from Bio.SeqIO.FastaIO import SimpleFastaParser

# create empty list for sequences from the fasta file to be added to
sequences = []

# open fasta file for reading 
with open('immune_proteins.fasta', 'r') as f:

    # iterate through tuples in SimpleFastaParser class instance 
    for header, sequence in SimpleFastaParser(f):

        # split the header on character into a list of strings
        header_parts = header.split("|")
        
        # create entry (dictionary) for each sequence with accession, sequence, and sequence length info
        entry = {
            "accession_id": header_parts[1],
            "sequence": sequence,
            "sequence_length": len(sequence)
        }

        # add the entry to the list of sequences
        sequences.append(entry)

# set total residues from fasta sequences to 0
total_residues = 0

# set longest and shortest accessions and their lengths to that of first sequence in list
longest_accession_length = sequences[0]['sequence_length']
longest_accession = sequences[0]['accession_id']
shortest_accession_length = sequences[0]['sequence_length']
shortest_accession = sequences[0]['accession_id']

# iterate through entries in the sequences list
for seq in sequences:

    # add the number of residues of the current sequence to total residues
    total_residues += seq['sequence_length']

    # if this sequence is the longest so far, set longest accession and its length 
    if seq['sequence_length'] > longest_accession_length:
        longest_accession_length = seq['sequence_length']
        longest_accession = seq['accession_id']
    
    # if this sequence is the shortest so far, set shortest accession and its length 
    if seq['sequence_length'] < shortest_accession_length:
        shortest_accession_length = seq['sequence_length']
        shortest_accession = seq['accession_id']

# print results
print(f"Num Sequences: {len(sequences)}")
print(f"Total Residues: {total_residues}")
print(f"Longest Accession: {longest_accession} ({longest_accession_length} residues)")
print(f"Shortest Accession: {shortest_accession} ({shortest_accession_length} residues)")
