#!/usr/bin/env python3
import argparse
import logging
import socket
import sys
from Bio.SeqIO.FastaIO import SimpleFastaParser

# -------------------------
# Constants (configuration)
# -------------------------
OUTPUT_FASTA = 'long_only.fasta'
MINIMUM_LENGTH = 1000

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
    '-f', '--fastafile',
    type=str,
    required=True,
    help='The path to the input FASTA file'
)
parser.add_argument(
    '-o', '--output',
    type=str,
    required= False,
    default=OUTPUT_FASTA,
    help=f'The path to the output FASTA file (default: {OUTPUT_FASTA})'
)
parser.add_argument(
    '-m', '--minimumLength',
    type=int,
    required= False,
    default=MINIMUM_LENGTH,
    help=f'The minimum length to filter by (default: {MINIMUM_LENGTH})'
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

def filter_fasta(input_file: str, output_file: str, min_length: int) -> None:
    """
    Given input FASTA file, output file path, and minimum sequence length, iterates through sequences and writes sequences greater than 
    or equal to minimum sequence length to output FASTA file.

    Args:
        input_file: path to input FASTA file
        output_file: path to output FASTA file
        min_length: minimum length of protein to filter sequences by

    Returns: 
        None: this function doesn't return anything; it writes filtered sequences to FASTA file
    """

    logging.info(f"Reading FASTA file '{input_file}' and writing filtered sequences to '{output_file}' given minimum length: {min_length}")

    # open given fasta file for reading and open new fasta file for writing
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        
        # iterate through tuples in SimpleFastaParser instance of given fasta file
        for header, sequence in SimpleFastaParser(infile):
            
            # if the length of the sequence is greater than 1000 residues, 
            # write the header on one line and the sequence on the next
            if len(sequence) >= min_length:
                outfile.write(f">{header}\n")
                outfile.write(f"{sequence}\n")

def main():
    
    logging.info("Starting FASTA filtering workflow")

    try:
        filter_fasta(args.fastafile, args.output, args.minimumLength)
    except FileNotFoundError:
        logging.error(f"Input FASTA file '{args.fastafile}' not found. Exiting.")
        sys.exit(1)

    logging.info("FASTA filtering workflow complete")

if __name__ == '__main__':
    main()