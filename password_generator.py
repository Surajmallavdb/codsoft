# password_generator.py

import random
import string

def password_generator():
    print("Password Generator")

    length = int(input("Enter the desired length of the password: "))

    # Define the characters that can be used in the password
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password
    password = ''.join(random.choice(all_characters) for _ in range(length))

    print(f"Generated Password: {password}")

if __name__ == "__main__":
    password_generator()