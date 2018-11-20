"""
Simple script to generate sense and antisense oligos for sgRNA.
Hard-coded for construct addgene #52628.
"""
import click

# All 5' to 3'
SGRNA = (  # The target sgRNA sequences - should be 20 BP
    "TCACCTGTCAGGAACACCAG",
    "AGGGGAGTTCCATGCCTGAT",
    "GTTAACTTCCCTCACCTGTC",
)
FORWARD_OVERHANG = "ACCG"  # The overhang that goes in front of the forward strand
REVERSE_OVERHANG = "AAAC"  # The overhang that goes in front of the reverse strand
NAME = "ITGA10_sgi"  # The base name constructs


def complement(base):
    """
    Return the complementary DNA base
    """
    complements = {"A": "T", "T": "A", "G": "C", "C": "G"}
    try:
        return complements[base]
    except KeyError:
        raise ValueError("Invalid DNA base. Must be uppercase ATGC")


def reverse_complement(seq):
    """
    Return the reverse complement DNA sequence
    """
    return "".join((complement(base) for base in reversed(seq)))


def make_oligos(sgrna, for_overhang, rev_overhang):
    """
    Takes sgrna, a 20 BP sequence representing the target for the sgRNA. The function
    returns the oligos that need to be ordered, with the appropriate overhangs. If the
    first base is G, it is omitted in favor of the G in the last position of the
    overhang. The returned oligos are either 24 or 23 bases each.
    """
    if len(sgrna) != 20:
        raise TypeError("The sgRNA sequence must be 20 BP long")
    if sgrna[0] == "G":  # Trim because there is G in overhang
        sgrna = sgrna[1:20]
    forward = for_overhang + sgrna
    reverse = rev_overhang + reverse_complement(sgrna)
    return forward, reverse


def print_oligo(forward, reverse, overhang=0):
    """
    prints forward and revese of short oligos with specified overhang.
    Positive overhang for 5' overhang, negative for 3'
    """
    reverse = reverse[::-1]
    if overhang > 0:
        reverse = " " * overhang + reverse
        forward = forward + " " * overhang
    if overhang < 0:
        reverse = reverse + " " * abs(overhang)
        forward = " " * abs(overhang) + forward
    rungs = [
        " " if (reverse[n] == " " or b == " ") else "|" for n, b in enumerate(forward)
    ]
    click.secho(" ".join(["5' -"] + list(forward) + ["- 3'"]), fg="green")
    click.secho(" " * 5 + " ".join(rungs), fg="white")
    click.secho(" ".join(["3' -"] + list(reverse) + ["- 5'"]), fg="red")


@click.command()
@click.option("--name", default=NAME)
@click.option("--for_overhang", default=FORWARD_OVERHANG)
@click.option("--rev_overhang", default=REVERSE_OVERHANG)
@click.argument("sgrnas", nargs=-1, required=False)
def main(name, for_overhang, rev_overhang, sgrnas):
    if len(sgrnas) == 0:
        sgrnas = SGRNA
    oligos = [make_oligos(sgrna, for_overhang, rev_overhang) for sgrna in sgrnas]
    click.echo("-" * 88 + "\n")
    for n, (forward, reverse) in enumerate(oligos):
        click.echo(name + f"{n+1}_forward: 5'-{forward}-3' ({len(forward)} bases)")
        click.echo(name + f"{n+1}_reverse: 5'-{reverse}-3'\n")
        print_oligo(forward, reverse, len(for_overhang))
        click.echo("-" * 88)
        click.echo("")


if __name__ == "__main__":  # pragma: no cover
    main()
