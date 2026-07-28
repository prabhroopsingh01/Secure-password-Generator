# Secure Password Generator

## Project Overview

The Secure Password Generator is a Python cybersecurity application that creates customizable passwords using cryptographically secure randomness.

GitHub is used for version control, branching, commits, pull requests, and code integration. Freshservice is used to create, assign, track, and resolve development tickets.

## Features

- Secure password generation
- Custom password lengths from 8 to 128 characters
- Lowercase letter option
- Uppercase letter option
- Number option
- Special character option
- Input validation
- Password strength assessment
- Automated tests

## Security Design

The application uses Python's `secrets` module instead of the standard `random` module because password generation is security-sensitive.

The generator ensures that at least one character from every selected category is included. The generated characters are then securely shuffled so that required character types do not appear in predictable positions.

## Requirements

- Python 3.10 or newer
- Git

No third-party Python packages are required.

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/Secure-password-Generator.git
```

Open the project folder:

```bash
cd Secure-password-Generator
```

Replace `YOUR-USERNAME` with your actual GitHub username.

## Run the Program

```bash
python password_generator.py
```

The program will ask you to:

1. Enter the desired password length.
2. Choose whether to include lowercase letters.
3. Choose whether to include uppercase letters.
4. Choose whether to include numbers.
5. Choose whether to include special characters.

The generated password and its strength rating will then be displayed.

## Run the Automated Tests

```bash
python -m unittest test_password_generator.py
```

A successful test run should end with:

```text
OK
```

## Branching Strategy

The project uses the following Git branching strategy:

- `main` contains the stable release version.
- `development` contains completed features being prepared for release.
- `feature/*` branches contain individual project features.

Each feature is developed on its own feature branch and merged into `development` through a pull request. After all features are completed and tested, `development` is merged into `main`.

## Freshservice Workflow

Freshservice tickets follow this workflow:

1. Open
2. In Progress
3. Resolved

The relevant Freshservice ticket number is included in Git commit messages and pull-request descriptions to connect development work with its corresponding task.

## Project Files

```text
Secure-password-Generator/
│
├── password_generator.py
├── test_password_generator.py
├── README.md
├── SECURITY.md
├── requirements.txt
└── docs/
    └── Freshservice_Guide.md
```

## Security Limitations

- Generated passwords are displayed as plain text in the terminal.
- The application does not save or transmit passwords.
- Users should immediately store generated passwords in a trusted password manager.
- The strength rating is educational and does not guarantee that a password cannot be compromised.

## Author

Prabhroop Singh