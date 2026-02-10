# import SimpleFastaParser class from Bio.SeqIO.FastaIO library
from Bio.SeqIO.FastaIO import SimpleFastaParser

# open given fasta file for reading and open new fasta file for writing
with open('immune_proteins.fasta', 'r') as infile, open('long_only.fasta', 'w') as outfile:
    
    # iterate through tuples in SimpleFastaParser instance of given fasta file
    for header, sequence in SimpleFastaParser(infile):
        
        # if the length of the sequence is greater than 1000 residues, 
        # write the header on one line and the sequence on the next
        if len(sequence) >= 1000:
            outfile.write(f">{header}\n")
            outfile.write(f"{sequence}\n")