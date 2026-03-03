#!/usr/bin/env python3
from Bio import Entrez, SeqIO
import redis
import json
import argparse
import logging
import socket
import sys

# -------------------------
# Constants (configuration)
# -------------------------
SEARCH_TERM = 'Arabidopsis thaliana AND AT5G10140'
OUTPUT_TXT = 'genbank_records.txt'
EMAIL = 'colinsedgwick@utexas.edu'

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
    '-o', '--output',
    type=str,
    required=False,
    default=OUTPUT_TXT,
    help=f'The path to the output TXT file (default: {OUTPUT_TXT})'
)
parser.add_argument(
    '-s', '--searchTerm',
    type=str,
    required=False,
    default=SEARCH_TERM,
    help=f'The search term used to retrieve GB records (default: {SEARCH_TERM})'
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
def retrieve_gb_records(search_term: str) -> list[object]:
    """
    Given input search term, searches NCBI protein database and uses GenBank IDs 
    to retrieve and build list of records.

    Args:
        search_term: a string corresponding to the search term(s) used in the database search

    Returns:
        list[object]: a list of SeqRecord objects
    """
    # email to be used in NCBI search
    Entrez.email = EMAIL

    logging.info(f"Searching NCBI protein database using search term: {search_term}")

    # search for records in NCBI protein database using input search term, returning 30 IDs max
    with Entrez.esearch(db="protein", term=search_term, retmax=30) as h:
        results = Entrez.read(h)
    
    # using the list of IDs from the search, join into a single string separated by commas
    single_string_id = ",".join(results["IdList"])

    # create an empty list of records
    rec_list = []

    logging.info(f"Retrieving GenBank records using found IDs")

    # retrieve records using the IDs, 
    # and iterate through each record, adding each to rec_list
    with Entrez.efetch(db="protein", id=single_string_id, rettype="gb", retmode="text") as h:
        for record in SeqIO.parse(h, "gb"):
            rec_list.append(record)

    # return the list of records
    return rec_list

def save_data_to_redis(records_list: list[object]) -> None:
    """
    Given an input list of SeqRecord objects, saves a summary of information about each record
    to a Redis database.

    Args: 
        records_list: a list of SeqRecord objects

    Returns:
        None: this function does not return a value; it saves key-value pairs to a Redis database
    """

    # create a Python client object to the Redis server
    rd=redis.Redis(host='127.0.0.1', port=6379, db=1)
    
    logging.info(f"Saving records to Redis database")

    # iterate through the records in the input list and save the ID as the key 
    # and a summary of the record in a JSON string as the value to Redis
    for record in records_list:
        rec_summary = {'ID': record.id, 'Name': record.name, 'Description': record.description, 'Sequence':str(record.seq)}
        rd.set(record.id, json.dumps(rec_summary))

def write_redis_data_to_txt(output_file: str) -> None:
    """
    Given output file name, writes Redis data to TXT file.

    Args:
        output_file: path of output TXT file

    Returns:
        None: this function doesn't return a value; it writes data to an output file
    """

    # create a Python client object to the Redis server
    rd=redis.Redis(host='127.0.0.1', port=6379, db=1)

    logging.info(f"Writing Redis data to output file {output_file}")

    # iterates through keys in Redis database, writing record summary value to outfile
    with open(output_file, "w") as outfile:
        for key in rd.keys():
            sum_dict = json.loads(rd.get(key))
            sum_string = f"ID: {sum_dict['ID']}\nName: {sum_dict['Name']}\nDescription: {sum_dict['Description']}\nSequence: {sum_dict['Sequence']}\n\n"
            outfile.write(sum_string)

def main():

    logging.info(f"Starting GenBank records retrieval workflow")
    
    try:
        rec_list = retrieve_gb_records(args.searchTerm)
        save_data_to_redis(rec_list)
        write_redis_data_to_txt(args.output)
    except redis.exceptions.ConnectionError:
        logging.error(f"Could not connect to Redis database. Exiting.")
        sys.exit(1)

    logging.info("GenBank records retrieval workflow complete")

if __name__ == '__main__':
    main()

