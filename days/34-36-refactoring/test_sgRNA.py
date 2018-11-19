import pytest

from sgRNA import main


def test_main(capsys):
    main()
    out, _ = capsys.readouterr()
    assert (
        out
        == "----------------------------------------------------------------------------------------\n\nITGA10_sgi1_forward: 5'-ACCGTCACCTGTCAGGAACACCAG-3' (24 bases)\nITGA10_sgi1_reverse: 5'-AAACCTGGTGTTCCTGACAGGTGA-3'\n\n5' - A C C G T C A C C T G T C A G G A A C A C C A G - 3'\n             | | | | | | | | | | | | | | | | | | | |\n3' -         A G T G G A C A G T C C T T G T G G T C C A A A - 5'\n----------------------------------------------------------------------------------------\n\nITGA10_sgi2_forward: 5'-ACCGAGGGGAGTTCCATGCCTGAT-3' (24 bases)\nITGA10_sgi2_reverse: 5'-AAACATCAGGCATGGAACTCCCCT-3'\n\n5' - A C C G A G G G G A G T T C C A T G C C T G A T - 3'\n             | | | | | | | | | | | | | | | | | | | |\n3' -         T C C C C T C A A G G T A C G G A C T A C A A A - 5'\n----------------------------------------------------------------------------------------\n\nITGA10_sgi3_forward: 5'-ACCGTTAACTTCCCTCACCTGTC-3' (23 bases)\nITGA10_sgi3_reverse: 5'-AAACGACAGGTGAGGGAAGTTAA-3'\n\n5' - A C C G T T A A C T T C C C T C A C C T G T C - 3'\n             | | | | | | | | | | | | | | | | | | |\n3' -         A A T T G A A G G G A G T G G A C A G C A A A - 5'\n----------------------------------------------------------------------------------------\n\n"
    )
