# Security Policy

## Supported Version

Only the latest version available on the `main` branch is officially supported.

## Reporting a Security Vulnerability

Security vulnerabilities should be reported privately to the project owner before public disclosure.

A vulnerability report should include:

- A clear description of the vulnerability
- Steps required to reproduce the issue
- The possible security impact
- Screenshots or error messages, when available
- A suggested correction, when available

Sensitive vulnerability information should not be posted publicly until the issue has been reviewed and corrected.

## Password Generation

The application uses Python's `secrets` module to generate passwords. This module is designed for cryptographically secure random values.

The application does not use Python's standard `random` module for password generation because it is not appropriate for security-sensitive purposes.

## Input Validation

The application validates:

- Password length
- Non-numeric password-length entries
- Yes-or-no responses
- Character category selection
- Minimum and maximum length requirements

## Password Handling

The application:

- Displays the generated password in the terminal
- Does not save generated passwords
- Does not transmit passwords
- Does not create password history files

Users should transfer generated passwords to a trusted password manager and avoid displaying them in public environments.

## Dependencies

The project uses only Python standard-library modules. No third-party packages are required.