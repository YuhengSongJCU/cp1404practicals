from guitar import Guitar

FILENAME = "guitars.csv"

def load_guitars(filename):
    """Load guitars from a CSV file."""
    guitars = []

    with open(filename, "r") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            name = parts[0].strip()
            year = int(parts[1])
            cost = float(parts[2])
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)

    return guitars

def display_guitars(guitars):
    """Display all guitars"""
    for guitar in guitars:
        print(guitar)

def main():
    guitars = load_guitars(FILENAME)
    guitars.sort()
    display_guitars(guitars)

    print("Enter your new guitars:")
    name = input("Name: ")

    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))

        guitar = Guitar(name, year, cost)
        guitars.append(guitar)

        print(f"{guitar} added.")
        name = input("Name: ")

    guitars.sort()

    with open(FILENAME, "w") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)

main()