"""Wimbledon champion statistics.
Estimate: 30 minutes
Actual:
"""

import csv

FILENAME = "wimbledon.csv"

def main():
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)
        records = list(reader)

    print(records[:3])


main()
