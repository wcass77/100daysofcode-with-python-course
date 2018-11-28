from collections import namedtuple
from typing import List

import requests

URL = "http://search.talkpython.fm/api/search?q="

Episode = namedtuple("Episode", ("category", "id", "url", "title", "description"))


def search(search_terms: List[str], item_type: str = "Episode") -> List[Episode]:
    param = "-".join(search_terms)
    results = requests.get(URL + param).json()
    results = [
        Episode(**result)
        for result in results["results"]
        if result["category"] == item_type
    ]
    if not results:
        raise NoResultsFound
    return results


class NoResultsFound(Exception):
    pass
