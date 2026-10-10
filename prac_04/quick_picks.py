import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45

def main():
    """Generate random quick picks."""
    number_of_picks = int(input("How many quick picks? "))

    for i in range(number_of_picks):
        quick_pick = []

        while len(quick_pick) < NUMBERS_PER_LINE:
            number = random.randint(MINIMUM, MAXIMUM)

            if number not in quick_pick:
                quick_pick.append(number)

        quick_pick.sort()
        print(" ".join(f"{number:2}" for number in quick_pick))

main()
