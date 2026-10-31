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

        guitars.sort()

        print("Enter your new guitars:")
        name = input("Name: ")

        while name != "":
            year = int(input("Year: "))
            cost = float(input("Cost: $"))

            guitar = Guitar(name, year, cost)
            guitars.append(guitar)

            print(f"{guitar} added.")
            name = input("Name: ")

main()