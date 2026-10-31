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

def add_guitars(guitars):
    """Get new guitars from the user."""
    print("Enter your new guitars:")
    name = input("Name: ")

    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))

        guitar = Guitar(name, year, cost)
        guitars.append(guitar)

        print(f"{guitar} added.")
        name = input("Name: ")

def save_guitars(guitars, filename):
    """Save guitars to a CSV file."""
    with open(filename, "w") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)

def main():
    guitars = load_guitars(FILENAME)
    guitars.sort()
    display_guitars(guitars)
    add_guitars(guitars)

    guitars.sort()
    save_guitars(guitars, FILENAME)


main()