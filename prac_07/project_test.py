from project import Project


def main():
    """Test project methods."""
    car_park = Project("Build Car Park", "12/09/2021", 2, 600000.0, 95)
    pantry = Project("Organise Pantry", "20/07/2022", 1, 100.0, 100)

    print(car_park)

    print(f"Car park complete - Expected False. Got {car_park.is_complete()}")
    print(f"Pantry complete - Expected True. Got {pantry.is_complete()}")

    projects = [car_park, pantry]
    projects.sort()

    print("Projects sorted by priority:")
    for project in projects:
        print(f"{project.priority}: {project.name}")


main()
