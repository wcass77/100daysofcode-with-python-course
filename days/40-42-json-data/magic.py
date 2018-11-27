import json
from pprint import pprint

import requests

URL = "https://api.magicthegathering.io/v1/sets"

r = requests.get(URL)
data = json.loads(r.text)
sets = data["sets"]
boosters = [set["booster"] for set in sets if "booster" in set.keys()]
booster_sizes = [len(booster) for booster in boosters]
print(
    f"The minimum number of booster cards is {min(booster_sizes)}"
    f" and the max is {max(booster_sizes)}"
)
