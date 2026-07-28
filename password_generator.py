"""Customizable secure password generator."""

import secrets
import string

MIN_LENGTH = 8
MAX_LENGTH = 128
DEFAULT_LENGTH = 12


def generate_password(
    length: int = DEFAULT_LENGTH,
    use_lowercase: bool = True,
    use_uppercase: bool = True,
    use_digits: bool = True,
    use_symbols: bool = True,
) -> str:
    """Generate a secure password using selected character categories."""
    if length < MIN_LENGTH or length > MAX_LENGTH:
        raise ValueError(
            f"Password length must be between {MIN_LENGTH} and {MAX_LENGTH}."
        )

    categories: list[str] = []

    if use_lowercase:
        categories.append(string.ascii_lowercase)

    if use_uppercase:
        categories.append(string.ascii_uppercase)

    if use_digits:
        categories.append(string.digits)

    if use_symbols:
        categories.append(string.punctuation)

    if not categories:
        raise ValueError("At least one character category must be selected.")

    if length < len(categories):
        raise ValueError(
            "Password length is too short for the selected categories."
        )

    password_characters = [
        secrets.choice(category)
        for category in categories
    ]

    all_characters = "".join(categories)

    password_characters.extend(
        secrets.choice(all_characters)
        for _ in range(length - len(password_characters))
    )

    secrets.SystemRandom().shuffle(password_characters)

    return "".join(password_characters)


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


def get_yes_no(question: str) -> bool:
    """Prompt the user until a valid yes-or-no answer is entered."""
    while True:
        answer = input(f"{question} (y/n): ").strip().lower()

        if answer in {"y", "yes"}:
            return True

        if answer in {"n", "no"}:
            return False

        print("Invalid selection. Please enter y or n.")


def get_character_options() -> tuple[bool, bool, bool, bool]:
    """Collect the character categories selected by the user."""
    while True:
        use_lowercase = get_yes_no("Include lowercase letters")
        use_uppercase = get_yes_no("Include uppercase letters")
        use_digits = get_yes_no("Include numbers")
        use_symbols = get_yes_no("Include special characters")

        if any(
            (
                use_lowercase,
                use_uppercase,
                use_digits,
                use_symbols,
            )
        ):
            return (
                use_lowercase,
                use_uppercase,
                use_digits,
                use_symbols,
            )

        print("\nSelect at least one character category.\n")


def main() -> None:
    """Run the customizable password generator."""
    print("Secure Password Generator")
    print("-------------------------")

    length = get_password_length()

    (
        use_lowercase,
        use_uppercase,
        use_digits,
        use_symbols,
    ) = get_character_options()

    password = generate_password(
        length=length,
        use_lowercase=use_lowercase,
        use_uppercase=use_uppercase,
        use_digits=use_digits,
        use_symbols=use_symbols,
    )

    print(f"\nGenerated password: {password}")


if __name__ == "__main__":
    main()
    