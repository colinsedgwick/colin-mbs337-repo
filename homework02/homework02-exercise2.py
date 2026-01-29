# import Seq class from Bio.Seq library
from Bio.Seq import Seq

# create an object of Seq class using given DNA sequence
dna_sequence = Seq("GAACCGGGAGGTGGGAATCCGTCACATATGAGAAGGTATTTGCCCGATAA")

# use .count() method to count amount of G and C within sequence
g_count = dna_sequence.count("G")
c_count = dna_sequence.count("C")

# determine total number of bases in sequence
total_bases = len(dna_sequence)

# print the percentage of bases that are G and C
print(f"{(g_count + c_count)/ total_bases*100}%")