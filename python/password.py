# imports
import random
import string

# function: generate the password
def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ''

    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not any([use_letters, use_numbers, use_symbols]):
        print("Please select at least one character type.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

#function: main entry point
def main():
    print("Welcome to the Password Generator!")

    while True:
        try:
            length = int(input("Please enter the length of the password: "))
            break
        except ValueError:
            print("Please enter a valid integer.")

    use_letters = input("Include letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, use_letters, use_numbers, use_symbols)

    if password:
        print("Your generated password:", password)


if __name__ == "__main__":
    main()