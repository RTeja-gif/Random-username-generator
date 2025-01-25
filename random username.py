import random
import string

def generate_username(adjectives, nouns, include_numbers=False, include_special_chars=False, length=None):
    """
    Generate a random username by combining an adjective and a noun.
    Optional customization for numbers, special characters, and length.
    """
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    username = adjective + noun

    # Add numbers if requested
    if include_numbers:
        number = str(random.randint(0, 999))
        username += number

    # Add special characters if requested
    if include_special_chars:
        special_char = random.choice(string.punctuation)
        username += special_char

    # Adjust length if specified
    if length and length > len(username):
        extra_chars = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length - len(username)))
        username += extra_chars

    return username

def save_usernames_to_file(usernames, filename="usernames.txt"):
    """Save a list of usernames to a text file."""
    with open(filename, "w") as file:
        for username in usernames:
            file.write(username + "\n")

def main():
    """Interactive script for generating random usernames."""
    adjectives = ["Cool", "Happy", "Fast", "Smart", "Brave", "Kind", "Quick", "Lucky"]
    nouns = ["Tiger", "Dragon", "Eagle", "Panda", "Lion", "Falcon", "Wolf", "Bear"]

    print("Welcome to the Random Username Generator!")

    # Get user preferences
    include_numbers = input("Would you like to include numbers in the username? (yes/no): ").lower() == "yes"
    include_special_chars = input("Would you like to include special characters? (yes/no): ").lower() == "yes"
    length = input("Enter desired username length (or press Enter to skip): ")
    length = int(length) if length.isdigit() else None

    num_usernames = int(input("How many usernames would you like to generate? "))

    # Generate usernames
    usernames = [
        generate_username(adjectives, nouns, include_numbers, include_special_chars, length)
        for _ in range(num_usernames)
    ]

    # Display usernames
    print("\nGenerated Usernames:")
    for username in usernames:
        print(username)

    # Save to file
    save_to_file = input("Would you like to save these usernames to a file? (yes/no): ").lower() == "yes"
    if save_to_file:
        filename = input("Enter the filename to save to (default: usernames.txt): ") or "usernames.txt"
        save_usernames_to_file(usernames, filename)
        print(f"Usernames saved to {filename}.")

if __name__ == "__main__":
    main()
