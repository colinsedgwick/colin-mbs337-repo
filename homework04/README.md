# Exercise 1  
This script reads a fasta file and iterates through and creates data entries for the sequences which are added to a list. It then iterates through this list to determine the total residues and longest and shortest sequences, and then it prints the number of sequences, total residues, and the accession IDs of the longest and shortest sequences from the sequences in the file.  
# Exercise 2  
This script reads an input fasta file and filters for sequences greater than or equal to 1000 residues that it writes to a new fasta file.  
# Exercise 3  
This script reads an input fastq file and filters for reads with average Phred scores of at least 30 to be written to a new fastq file, and then it prints the total number of reads in the input file and the number that were written to the new file.  
# Exercise 4  
This script reads and parses an mmCIF file for the protein structure and iterates over the hierarchy of structure to determine and print the number of non-hetero residues and atoms in each chain.  
# Where to get input files  
The input files can be retrieved by downloading from the following URLs (using "wget" in terminal) and unzipping the downloaded zip files (using "gunzip").  
## FASTA  
https://github.com/TACC/mbs-337-sp26/raw/refs/heads/main/docs/unit03/sample-data/immune_proteins.fasta.gz  
## FASTQ  
https://github.com/TACC/mbs-337-sp26/raw/refs/heads/main/docs/unit03/sample-data/sample1_rawReads.fastq.gz  
## mmCIF  
https://files.rcsb.org/download/4HHB.cif.gz  