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

    champion_to_count = {}

    for record in records:
        champion = record[2]
        if champion in champion_to_count:
            champion_to_count[champion] += 1
        else:
            champion_to_count[champion] = 1

    for champion, count in champion_to_count.items():
        print(f"{champion}: {count}")

    countries = set()

    for record in records:
        countries.add(record[1])

    print()
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


main()
