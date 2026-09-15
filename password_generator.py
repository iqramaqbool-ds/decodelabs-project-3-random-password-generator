import string
import secrets


def generate_password(length):
    """Generate a cryptographically secure random password."""

    # Character groups required for a strong password
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # Complete character pool
    characters = lowercase + uppercase + digits + special

    # Guarantee at least one character from each important category
    password_characters = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(special)
    ]

    # Fill the remaining positions securely
    for _ in range(length - 4):
        password_characters.append(secrets.choice(characters))

    # Securely shuffle the generated characters
    secrets.SystemRandom().shuffle(password_characters)

    return ''.join(password_characters)


def main():
    print("================================")
    print("   Enterprise Password Generator")
    print("================================")
    print("Minimum password length: 15 characters")
    print("Enter the required password length.\n")

    while True:
        user_input = input("Enter password length: ")

        try:
            length = int(user_input)

            if length < 15:
                print("Password length must be at least 15 characters.\n")
                continue

            password = generate_password(length)

            print("\nGenerated Password:")
            print(password)
            print(f"Password Length: {len(password)} characters")

            break

        except ValueError:
            print("Invalid input. Please enter a whole number.\n")


if __name__ == "__main__":
    main()