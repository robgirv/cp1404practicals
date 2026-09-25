"""Get a valid password and print the same number of asterisks per character."""
MINIMUM_PASSWORD_LENGTH = 8
REDACTED_CHARACTER = "*"


def main():
    """Get a valid password and display the same number of asterisks per character."""
    password = get_valid_password(MINIMUM_PASSWORD_LENGTH)
    print_asterisks(password, REDACTED_CHARACTER)


def get_valid_password(minimum_password_length: int = 8) -> str:
    """Get password from the user, satisfying a minimum length requirement."""
    password = input("Password: ")
    while len(password) < minimum_password_length:
        print(f"Error: Password is too short. It must be longer than {minimum_password_length} characters.")
        password = input("Password: ")
    return password


def print_asterisks(password: str, redacted_character: str):
    """Print asterisks of the same length as a password."""
    print(redacted_character * len(password))


main()
