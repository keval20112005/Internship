import random
import string

def generate_password(length):
    # Define possible characters: letters, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        # Prompt the user for the password length
        length = int(input("Enter the desired password length: "))
        
        if length <= 0:
            print("Password length must be greater than zero.")
            return

        # Generate and display the password
        password = generate_password(length)
        print("Generated password:", password)

    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
