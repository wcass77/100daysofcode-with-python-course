import io
import sys

import pytest

from api import search
from program import main


@pytest.fixture(
    params=[
        (
            "Lektor",
            "Talk Python Search:\n"
            "Search:1. 68: Crossing the streams with Podcast.__init__\n"
            "2. 69: Write an Excellent Programming Blog\n"
            "3. 160: Lektor: Beautiful websites out of flat files\n",
        ),
        ("zzzzzzz", "Talk Python Search:\nSearch:No results found for zzzzzzz\n"),
    ]
)
def mock_input(request):
    std_in_old = sys.stdin
    sys.stdin = io.StringIO(request.param[0])
    yield request.param[1]
    sys.stdin = std_in_old


@pytest.mark.parametrize(
    "search_terms, expected_results", [(["Lektor"], (68, 69, 160))]
)
def test_search(search_terms, expected_results):
    results = search(search_terms)
    result_ids = [r["id"] for r in results]

    assert len(result_ids) == len(expected_results)
    for id in result_ids:
        assert id in expected_results
    assert len(set(result_ids)) == len(result_ids)


def test_main(mock_input, capfd):
    main()
    output, _ = capfd.readouterr()
    assert output == mock_input
