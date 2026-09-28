MENU = """(G) Get a valid score
(P) Print result
(S) Show stars
(Q) Quit"""

def main():
    score = get_valid_score()

    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "G":
            score = get_valid_score()

        elif choice == "P":
            result = determine_score_result(score)
            print(result)

        elif choice == "S":
            print("*" * int(score))

        else:
            print("Invalid choice")

        print(MENU)
        choice = input(">>> ").upper()

    print("Farewell.")


def get_valid_score():
    score = float(input("Enter score: "))

    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))

    return score


def determine_score_result(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()