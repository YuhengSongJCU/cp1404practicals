"""
Emails
Estimate: 20 minutes
Actual:
"""

def extract_name(email):
    """Extract a name from an email address."""
    username = email.split("@")[0]
    name_parts = username.split(".")
    name = " ".join(name_parts).title()
    return name

# email = input("Email: ")
# print(extract_name(email))

email_to_name = {}

email = input("Email: ")
while email != "":
    name = extract_name(email)
    confirmation = input(f"Is your name {name}? (Y/N) ")

    if confirmation != "" and confirmation.upper() != "Y":
        name = input("Name: ")

    email_to_name[email] = name
    email = input("Email: ")

print()
for email, name in email_to_name.items():
    print(f"{name} ({email})")