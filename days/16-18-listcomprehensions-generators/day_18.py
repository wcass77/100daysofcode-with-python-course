# Bite 5 https://codechalleng.es/bites/5/

NAMES = [
    "arnold schwarzenegger",
    "alec baldwin",
    "bob belderbos",
    "julian sequeira",
    "sandra bullock",
    "keanu reeves",
    "julbob pybites",
    "bob belderbos",
    "julian sequeira",
    "al pacino",
    "brad pitt",
    "matt damon",
    "brad pitt",
]


def dedup_and_title_case_names(names):
    """Should return a list of names, each name appears only once"""
    return list({name.title() for name in names})


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    split_names = [name.split() for name in names]
    split_names.sort(key=lambda name: name[1].lower(), reverse=True)
    return [" ".join(name) for name in split_names]


def shortest_first_name(names):
    """Returns the shortest first name (str)"""
    names = dedup_and_title_case_names(names)
    return sorted([name.split()[0] for name in names], key=lambda name: len(name))[0]


# Tests


def test_dedup_and_title_case_names():
    names = dedup_and_title_case_names(NAMES)
    assert names.count("Bob Belderbos") == 1
    assert names.count("julian sequeira") == 0
    assert names.count("Brad Pitt") == 1
    assert len(names) == 10
    assert all(n.title() in names for n in NAMES)


def test_sort_by_surname_desc():
    names = sort_by_surname_desc(NAMES)
    assert names[0] == "Julian Sequeira"
    assert names[-1] == "Alec Baldwin"


def test_shortest_first_name():
    assert shortest_first_name(NAMES) == "Al"


# Bite 26 https://codechalleng.es/bites/26/

bites = {
    6: "PyBites Die Hard",
    7: "Parsing dates from logs",
    9: "Palindromes",
    10: "Practice exceptions",
    11: "Enrich a class with dunder methods",
    12: "Write a user validation function",
    13: "Convert dict in namedtuple/json",
    14: "Generate a table of n sequences",
    15: "Enumerate 2 sequences",
    16: "Special PyBites date generator",
    17: "Form teams from a group of friends",
    18: "Find the most common word",
    19: "Write a simple property",
    20: "Write a context manager",
    21: "Query a nested data structure",
}
exclude_bites = {6, 10, 16, 18, 21}


def filter_bites(bites=bites, bites_done=exclude_bites):
    """return the bites dict with the exclude_bites filtered out"""
    pass


# Tests


def test_filter_bites():
    result = filter_bites()
    assert type(result) == dict
    assert len(result) == 10
    for bite in exclude_bites:
        assert bite not in result, f"Bite {bite} should not be in result"


if __name__ == "__main__":
    test_dedup_and_title_case_names()
    test_sort_by_surname_desc()
    test_shortest_first_name()
    print("Tests Pass!")
