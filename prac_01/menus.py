user_name = input("Enter your name: ")

MENU = """(H) Hello
(G) Goodbye
(Q) Quit"""

print(MENU)
choice = input("Enter your choice: ")
while choice != "Q":
    if choice == "H":
        print(f"Hello {user_name}")
    elif choice == "G":
        print(f"Goodbye {user_name}")
    else:
        print("Invalid Choice")

    print(MENU)
    choice =input(">>>").upper()

print("Finished")