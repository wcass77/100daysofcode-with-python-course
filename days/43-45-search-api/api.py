import json
from typing import List

import requests

URL = "http://search.talkpython.fm/api/search?q="


def search(search_terms: List[str], item_type: str = "Episode") -> List[dict]:
    param = "-".join(search_terms)
    results = json.loads(requests.get(URL + param).text)
    results = [
        result for result in results["results"] if result["category"] == item_type
    ]
    if not results:
        raise NoResultsFound
    return results


class NoResultsFound(Exception):
    pass
