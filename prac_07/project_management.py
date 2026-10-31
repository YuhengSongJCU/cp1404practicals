from project import Project

FILENAME = "projects.txt"
MENU = """- (L)Load projects
- (S)Save projects
- (D)Display projects
- (F)Filter projects by date
- (A)Add new project
- (U)Update project
- (Q)Quit"""


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

def display_projects(projects):
    """Display incomplete and completed projects by priority."""
    incomplete_projects = []
    completed_projects = []

    for project in projects:
        if project.is_complete():
            completed_projects.append(project)
        else:
            incomplete_projects.append(project)

    incomplete_projects.sort()
    completed_projects.sort()

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"  {project}")

    print("Completed projects:")
    for project in completed_projects:
        print(f"  {project}")

def main():
    """Manage projects."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")

    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "D":
            display_projects(projects)
        else:
            print("This option is not implemented yet.")

        print(MENU)
        choice = input(">>> ").upper()

    print("Thank you for using Pythonic Project Management.")


main()
