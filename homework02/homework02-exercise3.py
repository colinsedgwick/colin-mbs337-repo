# function that counts percentage of each base in a sequence and returns dictionary with the data
def base_percentage(sequence):
    a_count = sequence.count("A")
    t_count = sequence.count("T")
    c_count = sequence.count("C")
    g_count = sequence.count("G")
    total_bases = len(sequence)

    base_dict = {"A": f"{a_count/total_bases*100:.2f}%",
                 "T": f"{t_count/total_bases*100:.2f}%",
                 "C": f"{c_count/total_bases*100:.2f}%",
                 "G": f"{g_count/total_bases*100:.2f}%"}
    
    return base_dict

# imports Seq class from Bio.Seq library
from Bio.Seq import Seq

# creates a DNA sequence using Seq() class
dna_sequence = Seq("GAACCGGGAGGTGGGAATCCGTCACATATGAGAAGGTATTTGCCCGATAA")

# prints the results of function with given sequence as input
print(base_percentage(dna_sequence))