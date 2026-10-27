"""
CP1404 Prac 5: Emails
Estimate: 20 minutes
Actual: 7 minutes
"""

email_to_name = {}

email = input("Email: ")
while email != "":
    name = email.split('@')[0]
    user_input = input(f"Is your name {name}? (Y/n) ").lower()
    if not user_input == "" and not user_input == "y":
        name = input("Name: ")
    email_to_name[email] = name
    email = input("Email: ")

for email, name in email_to_name.items():
    print(f"{name} ({email})")
