"""Basic secure password generator."""

import secrets
import string


def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(secrets.choice(characters) for _ in range(length))


def main():
    password = generate_password()
    print(f"Generated password: {password}")


if __name__ == "__main__":
    main()
