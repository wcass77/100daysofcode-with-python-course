import itertools
import os
import urllib.request

import pytest

# Bite 64 https://codechalleng.es/bites/64/


names = "Tim Bob Julian Carmen Sofia Mike Kim Andre".split()
locations = "DE ES AUS NL BR US".split()
confirmed = [False, True, True, False, True]


def get_attendees():
    for participant in itertools.zip_longest(
        names, locations, confirmed, fillvalue="-"
    ):
        print(participant)


# Tests


def test_get_attendees(capfd):
    get_attendees()
    output = capfd.readouterr()[0].strip().split("\n")

    assert len(output) == 8
    assert "('Kim', '-', '-')" in output
    assert "('Andre', '-', '-')" in output


# Bite 17 https://codechalleng.es/bites/17/


def friends_teams(friends, team_size=2, order_does_matter=False):
    if order_does_matter:
        teams = itertools.permutations(friends, team_size)
    else:
        teams = itertools.combinations(friends, team_size)
    yield from teams


# Tests


friends = "Bob Dante Julian Martin".split()


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (("Bob", "Dante"), True),
        (("Bob", "Julian"), True),
        (("Bob", "Martin"), True),
        (("Dante", "Julian"), True),
        (("Dante", "Martin"), True),
        (("Julian", "Martin"), True),
        # order does not matter
        (("Dante", "Bob"), False),
        (("Julian", "Bob"), False),
        (("Martin", "Bob"), False),
        (("Julian", "Dante"), False),
        (("Martin", "Dante"), False),
        (("Martin", "Julian"), False),
        # not with self
        (("Julian", "Julian"), False),
    ],
)
def test_team_of_two_order_does_not_matter(test_input, expected):
    """First test lists all combos"""
    combos = list(friends_teams(friends, team_size=2, order_does_matter=False))
    assert len(combos) == 6
    if expected:
        assert test_input in combos
    else:
        assert test_input not in combos


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (("Bob", "Dante"), True),
        (("Dante", "Julian"), True),
        (("Dante", "Martin"), True),
        # order does matter
        (("Dante", "Bob"), True),
        (("Julian", "Dante"), True),
        (("Martin", "Dante"), True),
    ],
)
def test_team_of_two_order_does_matter(test_input, expected):
    """From here on just test a subset of combos"""
    combos = list(friends_teams(friends, team_size=2, order_does_matter=True))
    assert len(combos) == 12
    assert test_input in combos


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (("Bob", "Dante", "Julian"), True),
        (("Bob", "Dante", "Martin"), True),
        (("Bob", "Julian", "Martin"), True),
        (("Dante", "Julian", "Martin"), True),
        # order does not matter
        (("Dante", "Bob", "Martin"), False),
        (("Julian", "Martin", "Dante"), False),
        # no one goes twice
        (("Dante", "Dante", "Martin"), False),
    ],
)
def test_team_of_three_order_does_not_matter(test_input, expected):
    combos = list(friends_teams(friends, team_size=3, order_does_matter=False))
    assert len(combos) == 4
    if expected:
        assert test_input in combos
    else:
        assert test_input not in combos


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (("Bob", "Dante", "Julian"), True),
        (("Bob", "Dante", "Martin"), True),
        (("Bob", "Julian", "Martin"), True),
        (("Dante", "Julian", "Martin"), True),
        # order does matter
        (("Dante", "Bob", "Martin"), True),
        (("Julian", "Martin", "Dante"), True),
    ],
)
def test_team_of_three_order_does_matter(test_input, expected):
    combos = list(friends_teams(friends, team_size=3, order_does_matter=True))
    assert len(combos) == 24
    assert test_input in combos


# Bite 65 https://codechalleng.es/bites/65/


# PREWORK
DICTIONARY = os.path.join("/tmp", "dictionary.txt")
urllib.request.urlretrieve("http://bit.ly/2iQ3dlZ", DICTIONARY)

with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])


def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    return _get_permutations_draw(draw).intersection(dictionary)


def _get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    all_permutations = itertools.permutations(draw, 1)
    for r in range(2, len(draw) + 1):
        all_permutations = itertools.chain(
            all_permutations, itertools.permutations(draw, r)
        )
    return set(map(lambda letters: "".join(letters).lower(), all_permutations))


# Tests

scrabble_scores = [
    (1, "E A O I N R T L S U"),
    (2, "D G"),
    (3, "B C M P"),
    (4, "F H V W Y"),
    (5, "K"),
    (8, "J X"),
    (10, "Q Z"),
]
LETTER_SCORES = {
    letter: score for score, letters in scrabble_scores for letter in letters.split()
}


def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


@pytest.mark.parametrize(
    "draw, expected",
    [
        ("T, I, I, G, T, T, L", "gilt"),
        ("O, N, V, R, A, Z, H", "zonar"),
        ("E, P, A, E, I, O, A", ("apio", "peai")),
        ("B, R, C, O, O, E, O", "boce"),
        ("G, A, R, Y, T, E, V", "garvey"),
    ],
)
def test_max_word(draw, expected):
    draw = draw.split(", ")
    words = get_possible_dict_words(draw)
    if len(expected) > 1:
        assert max_word_value(words) in expected
    else:
        assert max_word_value(words) == expected


if __name__ == "__main__":
    get_attendees()
