"""Secure password generator with custom password length."""

import secrets
import string

MIN_LENGTH = 8
MAX_LENGTH = 128
DEFAULT_LENGTH = 12


def generate_password(length: int = DEFAULT_LENGTH) -> str:
    """Generate a secure password of the requested length."""
    if length < MIN_LENGTH or length > MAX_LENGTH:
        raise ValueError(
            f"Password length must be between {MIN_LENGTH} and {MAX_LENGTH}."
        )

    characters = string.ascii_letters + string.digits + string.punctuation

    return "".join(
        secrets.choice(characters)
        for _ in range(length)
    )


def get_password_length() -> int:
    """Prompt the user until a valid password length is entered."""
    while True:
        user_input = input(
            f"Enter password length ({MIN_LENGTH}-{MAX_LENGTH}): "
        ).strip()

        try:
            length = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue

        if length < MIN_LENGTH:
            print(f"Password must contain at least {MIN_LENGTH} characters.")
        elif length > MAX_LENGTH:
            print(f"Password cannot exceed {MAX_LENGTH} characters.")
        else:
            return length


def main() -> None:
    """Run the password generator."""
    print("Secure Password Generator")
    print("-------------------------")

    length = get_password_length()
    password = generate_password(length)

    print(f"\nGenerated password: {password}")


if __name__ == "__main__":
    main()