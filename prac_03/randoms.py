import random

print(random.randint(5, 20))       # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))    # line 3

# Line 1:
# The smallest number is 5 and the largest number is 20.

# Line 2:
# The smallest number is 3 and the largest number is 9.
# It cannot produce 4.

# Line 3:
# The smallest number is 2.5 and the largest number is 5.5.

print(random.randint(1, 100))