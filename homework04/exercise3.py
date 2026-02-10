# import SeqIO class from Bio library
from Bio import SeqIO

# set number of infile and outfile reads to 0 and create empty list for records to be added to
infile_reads = 0
outfile_reads = 0
clean_records = []

# open given fastq file for reading
with open('sample1_rawReads.fastq', 'r') as infile:

    # iterate through sequence records in SeqIO.parse instance of given fastq file 
    # with Phred+33 quality encoding (fastq-sanger)
    for record in SeqIO.parse(infile, 'fastq-sanger'):
        
        # increment infile reads
        infile_reads += 1

        # retrieve phred quality scores and set to variable
        phred_scores = record.letter_annotations['phred_quality']
        
        # if the average phred score is greater than or equal to 30, add record to clean_records list
        # and increment outfile reads
        if sum(phred_scores)/len(phred_scores) >= 30:
            clean_records.append(record)
            outfile_reads += 1

# open new fastq file for writing and write clean_records to it in fastq format
with open('sample1_cleanReads.fastq', 'w') as outfile:
    SeqIO.write(clean_records, outfile, "fastq")

# print infile and outfile reads
print(f"Total reads in original file: {infile_reads}")
print(f"Reads passing filter: {outfile_reads}")