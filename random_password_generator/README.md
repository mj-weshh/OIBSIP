# Random Password Generator

This Python script provides a simple command-line interface to generate random passwords based on user preferences. Users can specify the length of the password and choose whether to include letters, digits, and symbols.

## Usage

1. Run the script using the following command:
   ```bash
   python random_password_generator.py
   ```

2. Follow the prompts to set your preferences:
   - Enter the preferred password length (e.g., 8).
   - Choose whether to include letters by entering 'Y' or 'N'.
   - Choose whether to include digits by entering 'Y' or 'N'.
   - Choose whether to include symbols by entering 'Y' or 'N'.

3. The script will generate and display a random password based on the provided preferences.

## Functionality

- The `password_generator` function takes user preferences (length, include_letters, include_digits, include_symbols) and generates a random password accordingly.
- User input is validated to ensure a valid password is generated.
- The script uses Python's `random` and `string` modules to create random passwords.
- The generated password is displayed to the user.
