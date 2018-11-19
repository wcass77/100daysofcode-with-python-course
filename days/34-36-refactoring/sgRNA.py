"""
Simple script to generate sense and antisense oligos for sgRNA.
Hard-coded for construct addgene #52628.
"""
# All 5' to 3'
SGRNA = [  # The target sgRNA sequences - should be 20 BP
    "TCACCTGTCAGGAACACCAG",
    "AGGGGAGTTCCATGCCTGAT",
    "GTTAACTTCCCTCACCTGTC",
]
SSOVERHANG = "ACCG"  # The overhang that goes in front of the forward strand
ASOVERHANG = "AAAC"  # The overhang that goes in front of the reverse strand
NAME = "ITGA10_sgi"


def complement(base):
    """
    Return the complementary DNA base
    """
    if base == "A":
        return "T"
    if base == "T":
        return "A"
    if base == "G":
        return "C"
    if base == "C":
        return "G"


def reverse_complement(seq):
    """
    Return the reverse complement DNA sequence
    """
    return "".join((complement(base) for base in reversed(seq)))


def make_oligos(sgrna):
    if len(sgrna) != 20:
        raise TypeError("The sgRNA sequence must be 20 BP long")
    if sgrna[0] == "G":  # Trim because there is G in overhang
        sgrna = sgrna[1:20]
    forward = SSOVERHANG + sgrna
    reverse = ASOVERHANG + reverse_complement(sgrna)
    return forward, reverse


def print_oligo(forward, reverse, overhang=0):
    """
    prints forward and revese of short oligos with specified overhang.
    Positive overhang for 5' overhang, negative for 3'
    """
    reverse = reverse[::-1]
    if overhang > 0:
        reverse = " " * overhang + reverse
    if overhang < 0:
        reverse = reverse + " " * overhang
    rungs = ["|" if reverse[n] != " " else " " for n, _ in enumerate(forward)]
    print("5' -", *forward, "- 3'")  # * unpacks so that there is a space between bases
    print(" " * 4, *rungs)
    print("3' -", *reverse, "- 5'")


if __name__ == "__main__":
    oligos = [make_oligos(sgrna) for sgrna in SGRNA]
    print("-" * 88 + "\n")
    for n, oligo in enumerate(oligos):
        print(NAME + f"{n+1}_forward: 5'-{oligo[0]}-3' ({len(oligo[0])} bases)")
        print(NAME + f"{n+1}_reverse: 5'-{oligo[1]}-3'\n")
        print_oligo(oligo[0], oligo[1], 4)
        print("-" * 88)
        print("")
