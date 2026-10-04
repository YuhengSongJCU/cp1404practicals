"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
A ValueError occurs when the input cannot be converted to an integer.
2. When will a ZeroDivisionError occur?
A ZeroDivisionError occurs when the denominator is 0.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes. Check that the denominator is not 0 before division.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")