# data/codon_bias.py
# Source: Codon Usage Database (kazusa.or.jp), Human data.
# Frequencies are per thousand.

HUMAN_CODON_BIAS = {
    'UUU': 17.6, 'UUC': 20.3, 'UUA': 7.7,  'UUG': 12.9, # Phe, Leu
    'CUU': 13.2, 'CUC': 19.6, 'CUA': 7.2,  'CUG': 39.6, # Leu
    'AUU': 16.0, 'AUC': 20.8, 'AUA': 7.5,  'AUG': 22.0, # Ile, Met
    'GUU': 11.0, 'GUC': 14.5, 'GUA': 7.1,  'GUG': 28.1, # Val
    'UCU': 15.2, 'UCC': 17.7, 'UCA': 12.2, 'UCG': 4.4,  # Ser
    'CCU': 17.5, 'CCC': 19.8, 'CCA': 16.9, 'CCG': 6.9,  # Pro
    'ACU': 13.1, 'ACC': 18.9, 'ACA': 15.1, 'ACG': 6.1,  # Thr
    'GCU': 18.4, 'GCC': 27.7, 'GCA': 15.8, 'GCG': 7.4,  # Ala
    'UAU': 12.2, 'UAC': 15.3, 'UAA': 1.0,  'UAG': 0.8,  # Tyr, STOP
    'CAU': 10.9, 'CAC': 15.1, 'CAA': 12.3, 'CAG': 34.2, # His, Gln
    'AAU': 17.0, 'AAC': 19.1, 'AAA': 24.4, 'AAG': 31.9, # Asn, Lys
    'GAU': 21.8, 'GAC': 25.1, 'GAA': 29.0, 'GAG': 39.0, # Asp, Glu
    'UGU': 10.6, 'UGC': 12.6, 'UGA': 1.6,  'UGG': 13.2, # Cys, STOP, Trp
    'CGU': 4.5,  'CGC': 10.4, 'CGA': 6.2,  'CGG': 11.4, # Arg
    'AGU': 12.1, 'AGC': 19.5, 'AGA': 12.2, 'AGG': 12.0, # Ser, Arg
    'GGU': 10.8, 'GGC': 22.2, 'GGA': 16.5, 'GGG': 16.5  # Gly
}
