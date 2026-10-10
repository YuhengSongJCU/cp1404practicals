"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Program to load and display subject data from file."""
    subjects = load_subjects(FILENAME)
    display_subjects(subjects)


def load_subjects(filename):
    """Read subject data from a file."""
    subjects = []

    with open(filename) as input_file:
        for line in input_file:
            parts = line.strip().split(",")
            subject = [parts[0], parts[1], int(parts[2])]
            subjects.append(subject)

    return subjects


def display_subjects(subjects):
    """Display details for each subject."""
    for subject in subjects:
        code, lecturer, students = subject
        print(f"{code} is taught by {lecturer:12} "
              f"and has {students:3} students")


main()