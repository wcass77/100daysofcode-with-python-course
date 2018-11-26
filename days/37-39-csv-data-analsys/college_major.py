"""
Dataset from fivethirtyeight
Article: https://fivethirtyeight.com/features/the-economic-guide-to-picking-a-college-major/
Repo: https://github.com/fivethirtyeight/data/tree/master/college-majors

Goals: load a subset of the data using the Dict Reader package, instead of pandas.
Answer question: Which major has the greatest spread between P25 and P75 in absolute and
relative terms?
"""
import csv
import os.path
from collections import namedtuple

import wget

Row = namedtuple("Row", ["Major", "P25th", "P75th", "spread", "ratio"])


DATA_FILE = "major_data.csv"
DATA_URL = "https://raw.githubusercontent.com/fivethirtyeight/data/master/college-majors/all-ages.csv"


def main():
    data_path = os.path.join(os.path.dirname(__file__), DATA_FILE)
    if not os.path.isfile(data_path):
        wget.download(DATA_URL, data_path)

    data = []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        data = [parse_row(row) for row in reader]
    print("Majors with the biggest spread (5):")
    for major in list(sorted(data, key=lambda x: -x.spread)[:5]):
        print(f"{major.Major}: {major.P25th} to {major.P75th}")
    print("Majors with the smallest spread (5):")
    for major in list(sorted(data, key=lambda x: x.spread)[:5]):
        print(f"{major.Major}: {major.P25th} to {major.P75th}")
    print("Majors with the biggest ratio (5):")
    for major in list(sorted(data, key=lambda x: -x.ratio)[:5]):
        print(f"{major.Major}: {major.P25th} to {major.P75th}")
    print("Majors with the smallest ratio (5):")
    for major in list(sorted(data, key=lambda x: x.ratio)[:5]):
        print(f"{major.Major}: {major.P25th} to {major.P75th}")


def parse_row(row):
    P25th = parse_int(row["P25th"])
    P75th = parse_int(row["P75th"])
    return Row(
        Major=row["Major"],
        P25th=P25th,
        P75th=P75th,
        spread=P75th - P25th,
        ratio=P75th / P25th,
    )


def parse_int(field: str):
    if "E" in field:
        coefficient, exponent = field.split("E")
        return int(float(coefficient) * 10 ** int(exponent))
    return int(field)


if __name__ == "__main__":
    main()
