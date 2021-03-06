import pytest
from click.testing import CliRunner

from sgRNA import (FORWARD_OVERHANG, REVERSE_OVERHANG, complement, main,
                   make_oligos, print_oligo, reverse_complement)


def test_main():
    result = CliRunner().invoke(main)

    assert (
        result.output
        == "----------------------------------------------------------------------------------------\n\n"
        "ITGA10_sgi1_forward: 5'-ACCGTCACCTGTCAGGAACACCAG-3' (24 bases)\n"
        "ITGA10_sgi1_reverse: 5'-AAACCTGGTGTTCCTGACAGGTGA-3'\n\n"
        "5' - A C C G T C A C C T G T C A G G A A C A C C A G         - 3'\n"
        "             | | | | | | | | | | | | | | | | | | | |        \n"
        "3' -         A G T G G A C A G T C C T T G T G G T C C A A A - 5'\n"
        "----------------------------------------------------------------------------------------\n\n"
        "ITGA10_sgi2_forward: 5'-ACCGAGGGGAGTTCCATGCCTGAT-3' (24 bases)\n"
        "ITGA10_sgi2_reverse: 5'-AAACATCAGGCATGGAACTCCCCT-3'\n\n"
        "5' - A C C G A G G G G A G T T C C A T G C C T G A T         - 3'\n"
        "             | | | | | | | | | | | | | | | | | | | |        \n"
        "3' -         T C C C C T C A A G G T A C G G A C T A C A A A - 5'\n"
        "----------------------------------------------------------------------------------------\n\n"
        "ITGA10_sgi3_forward: 5'-ACCGTTAACTTCCCTCACCTGTC-3' (23 bases)\n"
        "ITGA10_sgi3_reverse: 5'-AAACGACAGGTGAGGGAAGTTAA-3'\n\n"
        "5' - A C C G T T A A C T T C C C T C A C C T G T C         - 3'\n"
        "             | | | | | | | | | | | | | | | | | | |        \n"
        "3' -         A A T T G A A G G G A G T G G A C A G C A A A - 5'\n"
        "----------------------------------------------------------------------------------------\n\n"
    )


def test_complement():
    assert complement("A") == "T"
    assert complement("T") == "A"
    assert complement("C") == "G"
    assert complement("G") == "C"


def test_complement_invalid_bases():
    with pytest.raises(Exception):
        complement("U")
    with pytest.raises(Exception):
        complement("a")
    with pytest.raises(Exception):
        complement("X")
    with pytest.raises(Exception):
        complement("AC")


def test_reverse_complement():
    seq = "ATGCATGC"
    seq_rev_complement = "GCATGCAT"

    assert reverse_complement(seq) == seq_rev_complement
    assert reverse_complement(seq_rev_complement) == seq
    assert reverse_complement(reverse_complement(seq)) == seq


def test_reverse_complement_input():
    with pytest.raises(Exception):
        reverse_complement("acgt")
    with pytest.raises(Exception):
        reverse_complement("AUGC")
    with pytest.raises(Exception):
        reverse_complement("AC GT")
    with pytest.raises(Exception):
        reverse_complement("NATGC")


def test_make_oligos():
    sgrna = "ACGT" * 5
    forward, reverse = make_oligos(sgrna, FORWARD_OVERHANG, REVERSE_OVERHANG)

    assert len(forward) == 24
    assert len(reverse) == 24
    assert forward[0:4] == FORWARD_OVERHANG
    assert reverse[0:4] == REVERSE_OVERHANG
    assert forward[4:] == sgrna
    assert reverse[4:] == reverse_complement(sgrna)


def test_make_oligos_starting_G():
    sgrna = "GCAT" * 5
    forward, reverse = make_oligos(sgrna, FORWARD_OVERHANG, REVERSE_OVERHANG)

    assert len(forward) == 23
    assert len(reverse) == 23
    assert forward[0:4] == FORWARD_OVERHANG
    assert reverse[0:4] == REVERSE_OVERHANG
    assert forward[4:] == sgrna[1:]
    assert reverse[4:] == reverse_complement(sgrna[1:])


def test_make_oligos_bad_input():
    sgrnas = ("gcat" * 5, "GCAT" * 4, 20)
    for sgrna in sgrnas:
        with pytest.raises(Exception):
            make_oligos(sgrna, FORWARD_OVERHANG, REVERSE_OVERHANG)


def test_print_oligo_no_overhang(capfd):
    oligo = "AGTC" * 2
    rev_oligo = "GACT" * 2
    overhang = 0

    print_oligo(oligo, rev_oligo, overhang)
    output = capfd.readouterr().out

    assert output == (
        "5' - A G T C A G T C - 3'\n"
        "     | | | | | | | |\n"
        "3' - T C A G T C A G - 5'\n"
    )


def test_print_oligo_5_prime_overhang(capfd):
    oligo = "AGTC" * 2
    rev_oligo = "GACT" * 2
    overhang = 3

    print_oligo(oligo, rev_oligo, overhang)
    output = capfd.readouterr().out

    assert output == (
        "5' - A G T C A G T C       - 3'\n"
        "           | | | | |      \n"
        "3' -       T C A G T C A G - 5'\n"
    )


def test_print_oligo_3_prime_overhang(capfd):
    oligo = "AGTC" * 2
    rev_oligo = "GACT" * 2
    overhang = -3

    print_oligo(oligo, rev_oligo, overhang)
    output = capfd.readouterr().out

    assert output == (
        "5' -       A G T C A G T C - 3'\n"
        "           | | | | |      \n"
        "3' - T C A G T C A G       - 5'\n"
    )
