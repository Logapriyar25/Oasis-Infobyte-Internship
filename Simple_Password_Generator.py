import random
import string

def generate_password(length=12):
    # Characters to choose from: letters, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Ensure at least one character from each type is included
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    # Fill the rest of the password length
    password += random.choices(characters, k=length - 4)

    # Shuffle to avoid predictable pattern
    random.shuffle(password)

    return ''.join(password)

def main():
    print("=== Password Generator ===")
    try:
        length = int(input("Enter desired password length (minimum 8): "))
        if length < 8:
            print("Password length too short. Using default length of 12.")
            length = 12
    except ValueError:
        print("Invalid input. Using default length of 12.")
        length = 12

    password = generate_password(length)
    print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    main()
