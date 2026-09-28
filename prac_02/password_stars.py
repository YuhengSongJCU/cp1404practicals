MINIMUM_LENGTH = 5

password = input("Enter your password:")

while len(password) < MINIMUM_LENGTH:
    password = input("Enter your password:")

print("*"*len(password))