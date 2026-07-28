"""Basic secure password generator."""

import secrets
import string


def generate_password(length: int = 12) -> str:
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(secrets.choice(characters) for _ in range(length))


def main() -> None:
    password = generate_password()
    print(f"Generated password: {password}")


if __name__ == "__main__":
    main()
