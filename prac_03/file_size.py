def main():
    filename = input("Enter filename: ")

    while filename != "":
        number_of_lines = count_lines(filename)
        print(f"{filename} has {number_of_lines} lines.")
        filename = input("Enter filename: ")


def count_lines(filename):
    with open(filename, "r") as in_file:
        return len(in_file.readlines())


main()