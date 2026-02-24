#!/usr/bin/env python3
import argparse
import logging
import socket
import sys
from Bio.SeqIO.FastaIO import SimpleFastaParser

# -------------------------
# Constants (configuration)
# -------------------------
OUTPUT_TXT = 'proteins_stats.txt'

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
    default=OUTPUT_TXT,
    help=f'The path to the output TXT file (default: {OUTPUT_TXT})'
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

def retrieve_fasta_data(fasta_file: str) -> list:
    """
    Given an input FASTA file, parses through sequences and stores each sequence entry as a dictionary 
    and returns a list of the dictionaries. 

    Args: 
        fasta_file: path to the input FASTA file

    Returns: 
        list of sequence entries (dictionaries)
    """
    # create empty list for sequences from the fasta file to be added to
    sequences = []

    logging.info(f"Reading FASTA file '{fasta_file}'")

    # open fasta file for reading 
    with open(fasta_file, 'r') as f:

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

    logging.info(f"Finished reading {len(sequences)} reads")

    return sequences

def summarize_fasta_stats(fasta_data: list) -> str:
    """
    Given an input list of FASTA protein sequence entries, iterates through entries to determine
    fasta summary stats which are returned as a string.

    Args:
        fasta_data: a list of FASTA sequence entries

    Returns:
        string of FASTA data summary stats
    """
    
    logging.info(f"Creating summary statistics of FASTA data")

    # set total residues from fasta sequences to 0
    total_residues = 0

    # set longest and shortest accessions and their lengths to that of first sequence in list
    longest_accession_length = fasta_data[0]['sequence_length']
    longest_accession = fasta_data[0]['accession_id']
    shortest_accession_length = fasta_data[0]['sequence_length']
    shortest_accession = fasta_data[0]['accession_id']

    # iterate through entries in the sequences list
    for seq in fasta_data:

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

    summary = f"Num Sequences: {len(fasta_data)}\nTotal Residues: {total_residues}\nLongest Accession: {longest_accession} ({longest_accession_length} residues)\nShortest Accession: {shortest_accession} ({shortest_accession_length} residues)"

    return summary

def write_stats_to_txt(fasta_stats: str, output_file: str) -> None:
    """
    Given an input string of FASTA summary stats and a path to an output file, 
    writes summary stats to output file.

    Args:
        fasta_stats: string of FASTA summary stats
        output_file: path to the output file

    Returns:
        None: this function does not return a value; it writes to output file
    """
    logging.info(f"Writing summary statistics to {output_file}")

    with open(output_file, 'w') as o:
        o.write(fasta_stats)

def main():
    
    logging.info("Starting FASTA statistics workflow")

    try:
        protein_data = retrieve_fasta_data(args.fastafile)
        fasta_stats = summarize_fasta_stats(protein_data)
        write_stats_to_txt(fasta_stats, args.output)
    except FileNotFoundError:
        logging.error(f"Input FASTA file '{args.fastafile}' not found. Exiting.")
        sys.exit(1)

    logging.info("FASTA statistics workflow complete")

if __name__ == '__main__':
    main()

