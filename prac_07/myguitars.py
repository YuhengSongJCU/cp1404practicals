from guitar import Guitar

FILENAME = "guitars.csv"

def main():
    guitars = []
    with open(FILENAME, "r") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            name = parts[0].strip()
            year = int(parts[1])
            cost = float(parts[2])
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)

        for guitar in guitars:
            print(guitar)


main()