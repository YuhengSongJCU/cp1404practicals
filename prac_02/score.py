import random

def main():
    score = float(input("Enter your score: "))

    result = determine_score_result(score)
    print(f"User score{score} is {result}")

    if result == "Excellent" :
        print("Your get prize!")

    random_score = random.randint(0,100)
    random_result = determine_score_result(random_score)
    print(f"Random: {random_score} = {random_result}")


def determine_score_result(score):
    """Determine and return the result for a score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
