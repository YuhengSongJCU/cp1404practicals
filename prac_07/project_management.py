from project import Project

FILENAME = "projects.txt"


def load_projects(filename):
    """Load projects from a file."""
    projects = []

    with open(filename, "r") as in_file:
        next(in_file)
        for line in in_file:
            parts = line.strip().split("\t")
            project = Project(parts[0], parts[1], int(parts[2]),
                              float(parts[3]), int(parts[4]))
            projects.append(project)

    return projects


def main():
    """Manage projects."""
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")


main()
