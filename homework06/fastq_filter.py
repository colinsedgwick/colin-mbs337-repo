#!/usr/bin/env python3
import argparse
import logging
import socket
import sys
from Bio import SeqIO

# -------------------------
# Constants (configuration)
# -------------------------
OUTPUT_FASTQ = 'cleanReads.fastq'
ENCODING = 'fastq-sanger'
MINIMUM_PHRED = 30

# -------------------------
# Logging and Command Line Inputs setup
# -------------------------
parser = argparse.ArgumentParser()
parser.add_argument(
    '-l', '--loglevel',
    type=str,
    required=False,
    choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
    default='WARNING',
    help='set log level to DEBUG, INFO, WARNING, ERROR, or CRITICAL (default: WARNING)'
)
parser.add_argument(
    '-f', '--fastqfile',
    type=str,
    required=True,
    help='The path to the input FASTQ file'
)
parser.add_argument(
    '-o', '--output',
    type=str,
    required= False,
    default=OUTPUT_FASTQ,
    help=f'The path to the output FASTQ file (default: {OUTPUT_FASTQ})'
)
parser.add_argument(
    '-m', '--minimumPhred',
    type=int,
    required= False,
    default=MINIMUM_PHRED,
    help=f'The minimum average Phred score to filter by (default: {MINIMUM_PHRED})'
)
parser.add_argument(
    '-e', '--encoding',
    type=str,
    required= False,
    default=ENCODING,
    help=f'The encoding used for Phred scores (default: {ENCODING})'
)
args = parser.parse_args()

format_str = (
    f'[%(asctime)s {socket.gethostname()}] '
    '%(filename)s:%(funcName)s:%(lineno)s - %(levelname)s: %(message)s'
)
logging.basicConfig(level=args.loglevel, format=format_str)

# -------------------------
# Functions
# -------------------------

def filter_fastq(input_file: str, encoding: str, min_phred: int) -> list[object]:
    """
    Given input FASTQ file, Phred score encoding, and minimum phred score,
    filters reads with average Phred above input minimum from FASTQ file into returned list.

    Args:
        input_file: path to input FASTQ file
        encoding: Phred score encoding scheme
        min_phred: minimum Phred score to filter reads by
    
    Returns:
        list[SeqRecord]: a list of SeqRecord objects
    """

    # set number of infile and outfile reads to 0 and create empty list for records to be added to
    infile_reads = 0
    outfile_reads = 0
    clean_records = []

    logging.info(f"Reading FASTQ file '{input_file}'")

    # open given fastq file for reading
    with open(input_file, 'r') as infile:

        # iterate through sequence records in SeqIO.parse instance of given fastq file 
        # with Phred+33 quality encoding (fastq-sanger)
        for record in SeqIO.parse(infile, encoding):
            
            # increment infile reads
            infile_reads += 1

            # retrieve phred quality scores and set to variable
            phred_scores = record.letter_annotations['phred_quality']
            
            # if the average phred score is greater than or equal to 30, add record to clean_records list
            # and increment outfile reads
            if sum(phred_scores)/len(phred_scores) >= min_phred:
                clean_records.append(record)
                outfile_reads += 1
    
    logging.info(f"Finished reading FASTQ file '{input_file}")
    logging.info(f"Total reads in original file: {infile_reads}")
    logging.info(f"Reads passing filter: {outfile_reads}")

    return clean_records

def write_filtered_to_fastq(filtered_records: list[object], output_file: str) -> None:
    """
    Given a list of SeqRecord objects and output FASTQ file path, writes the reads to the output file
    in FASTQ format.

    Args:
        filtered_records: a list of SeqRecord objects to be written to output file
        output_file: path of output FASTQ file

    Returns:
        None: this function doesn't return a value; it writes to an output file
    """
    logging.info(f"Writing filtered records to {output_file}")

    # open new fastq file for writing and write clean_records to it in fastq format
    with open(output_file, 'w') as outfile:
        SeqIO.write(filtered_records, outfile, "fastq")

def main():

    logging.info("Starting FASTQ filter workflow")

    try:
        filtered_reads = filter_fastq(args.fastqfile, args.encoding, args.minimumPhred)
        write_filtered_to_fastq(filtered_reads, args.output)
    except FileNotFoundError:
        logging.error(f"Input FASTQ file '{args.fastqfile}' not found. Exiting.")
        sys.exit(1)

    logging.info("FASTQ filter workflow complete")

if __name__ == '__main__':
    main()