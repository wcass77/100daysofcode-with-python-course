us_state_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
}

states = [
    "Oklahoma",
    "Kansas",
    "North Carolina",
    "Georgia",
    "Oregon",
    "Mississippi",
    "Minnesota",
    "Colorado",
    "Alabama",
    "Massachusetts",
    "Arizona",
    "Connecticut",
    "Montana",
    "West Virginia",
    "Nebraska",
    "New York",
    "Nevada",
    "Idaho",
    "New Jersey",
    "Missouri",
    "South Carolina",
    "Pennsylvania",
    "Rhode Island",
    "New Mexico",
    "Alaska",
    "New Hampshire",
    "Tennessee",
    "Washington",
    "Indiana",
    "Hawaii",
    "Kentucky",
    "Virginia",
    "Ohio",
    "Wisconsin",
    "Maryland",
    "Florida",
    "Utah",
    "Maine",
    "California",
    "Vermont",
    "Arkansas",
    "Wyoming",
    "Louisiana",
    "North Dakota",
    "South Dakota",
    "Texas",
    "Illinois",
    "Iowa",
    "Michigan",
    "Delaware",
]

NOT_FOUND = "N/A"


def get_every_nth_state(states=states, n=10):
    """Return a list with every nth item (default argument n=10, so every
       10th item) of the states list above (remember: lists keep order)"""
    return [
        state for (state, i) in zip(states, range(len(states))) if ((i + 1) % n == 0)
    ]


def get_state_abbrev(state_name, us_state_abbrev=us_state_abbrev):
    """Look up a state abbreviation by querying the us_state_abbrev
       dict by full state name, for instance 'Alabama' returns 'AL',
       'Illinois' returns 'IL'.
       If the state is not in the dict, return 'N/A' which we stored
       in the NOT_FOUND constant (takeaway: dicts are great for lookups)"""
    try:
        return us_state_abbrev[state_name]
    except KeyError:
        return NOT_FOUND


def get_longest_state(data):
    """Receives data, which can be the us_state_abbrev dict or the states
       list (see above). It returns the longest state measured by the length
       of the string"""
    longest_state = ""
    for state in states:
        if len(state) > len(longest_state):
            longest_state = state
    return longest_state


def combine_state_names_and_abbreviations(
    us_state_abbrev=us_state_abbrev, states=states
):
    """Get the first 10 state abbreviations ('AL', 'AK', 'AZ', ...) from
       the us_state_abbrev dict, and the last 10 states from the states
       list (see above) and combine them into a new list without losing
       alphabetical order"""
    states = states.copy()
    states.sort()
    combined = [get_state_abbrev(state) for state in states[:10]] + states[-10:]
    return sorted(combined)


# Tests


def test_get_every_nth_state():
    expected = ["Massachusetts", "Missouri", "Hawaii", "Vermont", "Delaware"]
    assert list(get_every_nth_state()) == expected
    expected = ["Missouri", "Vermont"]
    assert list(get_every_nth_state(n=20)) == expected


def test_get_state_abbrev():
    assert get_state_abbrev("Illinois") == "IL"
    assert get_state_abbrev("North Dakota") == "ND"
    assert get_state_abbrev("bogus") == NOT_FOUND


def test_get_longest_state():
    # depending the direction of the sort (reversed or not)
    # both North and South Carolina are correct
    correct_answers = ("North Carolina", "South Carolina")
    assert get_longest_state(us_state_abbrev) in correct_answers
    assert get_longest_state(states) in correct_answers


def test_combine_state_names_and_abbreviations():
    expected = [
        "AK",
        "AL",
        "AR",
        "AZ",
        "CA",
        "CO",
        "CT",
        "DE",
        "FL",
        "GA",
        "South Dakota",
        "Tennessee",
        "Texas",
        "Utah",
        "Vermont",
        "Virginia",
        "Washington",
        "West Virginia",
        "Wisconsin",
        "Wyoming",
    ]
    assert combine_state_names_and_abbreviations() == expected


if __name__ == "__main__":
    test_get_every_nth_state()
    test_get_longest_state()
    test_get_state_abbrev()
    test_combine_state_names_and_abbreviations()
    print("Passed the tests!")
