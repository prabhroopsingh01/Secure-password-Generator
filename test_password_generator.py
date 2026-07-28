"""Automated tests for the Secure Password Generator."""

import string
import unittest

from password_generator import (
    assess_password_strength,
    generate_password,
)


class PasswordGeneratorTests(unittest.TestCase):
    """Test the password generator."""

    def test_requested_password_length(self):
        password = generate_password(length=20)
        self.assertEqual(len(password), 20)

    def test_default_password_length(self):
        password = generate_password()
        self.assertEqual(len(password), 12)

    def test_all_selected_categories_are_present(self):
        password = generate_password(length=20)

        self.assertTrue(any(c.islower() for c in password))
        self.assertTrue(any(c.isupper() for c in password))
        self.assertTrue(any(c.isdigit() for c in password))
        self.assertTrue(any(c in string.punctuation for c in password))

    def test_lowercase_only(self):
        password = generate_password(
            length=12,
            use_lowercase=True,
            use_uppercase=False,
            use_digits=False,
            use_symbols=False,
        )

        self.assertTrue(password.islower())
        self.assertTrue(password.isalpha())

    def test_invalid_short_length(self):
        with self.assertRaises(ValueError):
            generate_password(length=7)

    def test_invalid_long_length(self):
        with self.assertRaises(ValueError):
            generate_password(length=129)

    def test_no_character_categories(self):
        with self.assertRaises(ValueError):
            generate_password(
                length=12,
                use_lowercase=False,
                use_uppercase=False,
                use_digits=False,
                use_symbols=False,
            )

    def test_password_strength(self):
        strength = assess_password_strength("Abcdef123456!@#$")
        self.assertIn(strength, {"Strong", "Very Strong"})


if __name__ == "__main__":
    unittest.main()