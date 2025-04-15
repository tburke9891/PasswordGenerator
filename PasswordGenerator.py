######################################################################
# Password Generator by The Bannon Brothers!!!!
# Requirements:
#   Get all requirements from the user: length, uppercase, lowercase, digits, and special characters.
#   Define a function for all yes/no input parameters
#   Define a function to generate the password with the provided context
######################################################################

import secrets
import string

def get_input(prompt):
    while True:
        try:
            value = int(input(prompt + ": "))
            if value < 0:
                print("Please enter a non-negative number.")
            else:
                return value
        except ValueError:
            print("Please enter a valid number.")

def generate_password(length, num_upper, num_digits, num_special):
    if length < 6:
        raise ValueError("Password length must be at least 6.")

    num_lower = length - (num_upper + num_digits + num_special)
    if num_lower < 0:
        raise ValueError("Sum of uppercase, digits, and special characters exceeds total length.")

    # Character pools
    password = []
    password += [secrets.choice(string.ascii_uppercase) for i in range(num_upper)]
    password += [secrets.choice(string.digits) for i in range(num_digits)]
    password += [secrets.choice(string.punctuation) for i in range(num_special)]
    password += [secrets.choice(string.ascii_lowercase) for i in range(num_lower)]

    # Shuffle to avoid predictable order
    secrets.SystemRandom().shuffle(password)
    return ''.join(password)

# === Main Program ===
try:
    length = get_input("Enter total desired password length")
    num_upper = get_input("How many uppercase letters?")
    num_digits = get_input("How many digits?")
    num_special = get_input("How many special characters?")

    password = generate_password(length, num_upper, num_digits, num_special)
    print("\nGenerated password:", password)

except ValueError as e:
    print("Error:", e)