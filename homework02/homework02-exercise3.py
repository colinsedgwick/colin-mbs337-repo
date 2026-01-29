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

from Bio.Seq import Seq

dna_sequence = Seq("GAACCGGGAGGTGGGAATCCGTCACATATGAGAAGGTATTTGCCCGATAA")

print(base_percentage(dna_sequence))