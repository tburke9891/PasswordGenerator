######################################################################
# Password Generator by The Bannon Brothers!!!!
# Requirements:
#   Get all requirements from the user: length, uppercase, lowercase, digits, and special characters.
#   Define a function for all yes/no input parameters
#   Define a function to generate the password with the provided context
######################################################################

import secrets
import string

# function for all yes/no answers with the user input as the parameter
def get_yes_no(prompt):
    while True:
        choice = input(prompt + " (y/n): ").strip().lower()
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' or 'n'.")

# Generate the pasword with the user's input
def generate_password(length, use_upper, use_lower, use_digits, use_special):
    if length < 6:
        raise ValueError("Password length must be at least 6 characters.")

    char_pool = ""
    password = []

    if use_lower:
        char_pool += string.ascii_lowercase
        password.append(secrets.choice(string.ascii_lowercase))
    if use_upper:
        char_pool += string.ascii_uppercase
        password.append(secrets.choice(string.ascii_uppercase))
    if use_digits:
        char_pool += string.digits
        password.append(secrets.choice(string.digits))
    if use_special:
        char_pool += string.punctuation
        password.append(secrets.choice(string.punctuation))

    if not char_pool:
        raise ValueError("You must select at least one character type.")

    while len(password) < length:
        password.append(secrets.choice(char_pool))

    secrets.SystemRandom().shuffle(password)
    return ''.join(password)

# === Main Program ===
try:
    length = int(input("Enter desired password length: "))

    use_lower = get_yes_no("Include lowercase letters?")
    use_upper = get_yes_no("Include uppercase letters?")
    use_digits = get_yes_no("Include digits?")
    use_special = get_yes_no("Include special characters?")

    password = generate_password(length, use_upper, use_lower, use_digits, use_special)
    print("\nGenerated password:", password)

except ValueError as e:
    print("Error:", e)
