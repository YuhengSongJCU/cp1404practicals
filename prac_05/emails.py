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

email = input("Email: ")
print(extract_name(email))
