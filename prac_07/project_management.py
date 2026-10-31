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

def save_projects(projects, filename):
    """Save projects to a file."""
    with open(filename, "w") as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage",
              file=out_file)

        for project in projects:
            print(f"{project.name}\t{project.start_date}\t"
                  f"{project.priority}\t{project.cost_estimate}\t"
                  f"{project.completion_percentage}", file=out_file)

def add_project(projects):
    """Get a new project from the user."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))

    project = Project(name, start_date, priority,
                      cost_estimate, completion_percentage)
    projects.append(project)

def update_project(projects):
    """Update the completion percentage and priority of a project."""
    for index, project in enumerate(projects):
        print(f"{index} {project}")

    project_choice = int(input("Project choice: "))
    project = projects[project_choice]
    print(project)

    new_percentage = input("New Percentage: ")
    if new_percentage != "":
        project.completion_percentage = int(new_percentage)

    new_priority = input("New Priority: ")
    if new_priority != "":
        project.priority = int(new_priority)

def main():
    """Manage projects."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")

    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "L":
            filename = input("Filename: ")
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}")

        elif choice == "S":
            filename = input("Filename: ")
            save_projects(projects, filename)
            print(f"Saved {len(projects)} projects to {filename}")

        elif choice == "D":
            display_projects(projects)

        elif choice == "A":
            add_project(projects)

        elif choice == "U":
            update_project(projects)

        else:
            print("This option is not implemented yet.")

        print(MENU)
        choice = input(">>> ").upper()

    print("Thank you for using Pythonic Project Management.")


main()
