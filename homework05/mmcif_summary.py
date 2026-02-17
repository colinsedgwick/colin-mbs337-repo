import json
import argparse
import logging
import socket
import sys
from pydantic import BaseModel
from Bio.PDB.MMCIFParser import MMCIFParser

# -------------------------
# Constants (Configuration)
# -------------------------
MMCIF_FILE = "4HHB.cif"
STRUCTURE_ID = "hemoglobin"
OUTPUT_JSON = "4HHB_summary.json"

# -------------------------
# Logging setup
# -------------------------
parser = argparse.ArgumentParser()
parser.add_argument(
    '-l', '--loglevel',
    type=str,
    required=False,
    default='WARNING',
    help='set log level to DEBUG, INFO, WARNING, ERROR, or CRITICAL'
)
args = parser.parse_args()

format_str = (
    f'[%(asctime)s {socket.gethostname()}] '
    '%(filename)s:%(funcName)s:%(lineno)s - %(levelname)s: %(message)s'
)
logging.basicConfig(level=args.loglevel, format=format_str)

# -------------------------
# Classes
# -------------------------
class ChainSummary(BaseModel):
    chain_id: str
    total_residues: int
    standard_residues: int
    hetero_residue_count: int
    
class StructureSummary(BaseModel):
    chains: list[ChainSummary]

# -------------------------
# Functions
# -------------------------
def summarize_chain(chain: object) -> ChainSummary:
    """
    Given a chain object from the model of an MMCIF structure, 
    generate a summary of the residues in the chain.

    Args:
        chain: chain object from model of structure from MMCIF file

    Returns:
        ChainSummary: ChainSummary instance containing:
            Chain ID
            Total number of residues in chain
            Number of standard residues in chain
            Number of hetero residues in chain
    """
    
    logging.debug(f"Summarizing chain {chain.get_id()}")

    # set residue counts to 0
    total_res_count = 0
    stan_res_count = 0
    het_res_count = 0

    # iterate through each residue in the input chain and increment total count
    # and then check if residue is standard or hetero and increment appropriate count
    for residue in chain:
        total_res_count += 1
        hetfield, resseq, icode = residue.get_id()

        logging.debug(f"Analyzing residue {resseq}")

        if hetfield == " ":
            stan_res_count += 1
        else:
            het_res_count += 1

    # return ChainSummary object with appropriate summary information
    return ChainSummary(
        chain_id = chain.get_id(),
        total_residues = total_res_count,
        standard_residues = stan_res_count,
        hetero_residue_count = het_res_count
    )


def summarize_mmcif_structure(mmcif_file: str, structure_id: str = "structure_id") -> StructureSummary:
    """
    Given an MMCIF file and structure ID (optional), creates a list of ChainSummary instances 
    which are returned in a StructureSummary instance.

    Args:
        mmcif_file: the name of the mmcif file
        structure_id: the ID that will be used for the structure; has default value as ID of structure
                      is not important to purpose of this function
    
    Returns:
        StructureSummary: StructureSummary instance containing a list of ChainSummary objects
    """    

    # create an instance of MMCIFParser 
    parser = MMCIFParser()

    logging.info(f"Reading MMCIF file {mmcif_file}")

    # open input mmcif file for reading and retrieve structure as python variable 
    # with input (or default) structure id
    with open(mmcif_file, 'r') as f:
        structure = parser.get_structure(structure_id, f)
        if structure_id == "structure_id":
            logging.warning(f"No structure ID provided - defaulting to generic ID")

    # create empty list for ChainSummary objects to be added to
    chains_list = []

    # iterate through model(s) in structure
    for model in structure:

        # iterate through chains in model and append the returned ChainSummary object
        # from summarize_chain() function call to chains_list
        for chain in model:
            chains_list.append(summarize_chain(chain))
    
    logging.info(f"Finished summarizing {len(chains_list)} chains")

    # return StructureSummary object with list of ChainSummary objects
    return StructureSummary(
        chains = chains_list
    )


def write_summary_to_json(summary: StructureSummary, output_file: str) -> None:
    """
    Given a StructureSummary object instance and the name of an output file, 
    writes StructureSummary to output file in JSON format.

    Args:
        summary: a StructureSummary object containing list of ChainSummary objects
        output_file: name of output JSON file

    Returns:
        None
    """

    logging.info(f"Writing summary to {output_file}")

    # open json file for writing and write StructureSummary to it
    with open(output_file, 'w') as outfile:
        json.dump(summary.model_dump(), outfile, indent=2)

    logging.info(f"Finished writing {output_file}")

def main():
    
    logging.info(f"Starting MMCIF structure summary workflow")

    try: 
        # call summarize_mmcif_structure() function with MMCIF_FILE and STRUCTURE_ID constants as arguments
        # and set to 'summary' variable
        summary = summarize_mmcif_structure(MMCIF_FILE, STRUCTURE_ID)

        # call write_summary_to_json with 'summary' and OUTPUT_JSON constant as arguments
        write_summary_to_json(summary, OUTPUT_JSON)

        logging.info(f"MMCIF structure summary workflow complete!")
    
    # if incorrect MMCIF file name is input, produce an error message and terminate program
    except FileNotFoundError:
        logging.error(f"Input MMCIF file {MMCIF_FILE} not found. Exiting")
        sys.exit(1)


if __name__ == '__main__':
    main()

