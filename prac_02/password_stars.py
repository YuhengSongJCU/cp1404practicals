MINIMUM_LENGTH = 5

def main():
    password = get_password()
    print_stars(password)

def get_password():
    password = input("Enter your password:")
    while len(password) < MINIMUM_LENGTH:
        password = input("Enter your password:")
    return password

def print_stars(password):
    print("*" * len(password))

main()