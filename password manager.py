import string
import random

def password_storage(password,Service):
    # This function will handle the storage of passwords
    with open("passwords.txt", "a") as file:
        file.write(f"{Service}: {password}\n")
    print(f"Password for {Service} has been stored successfully.")


def application_home():
    #This is the main menu of the application
    print("Welcome to the Password Manager!")
    print("1. Generate Password")
    print("2. Store Password")
    print("3. View Stored Passwords")
    print("4. Exit")
    while True:
        choice = input("Please choose an option (1-4): ")
        if choice == '1':
            ask_command()
            application_home()
        elif choice == '2':
            Service = input("Enter the name of the service or account: ")
            password = input("Enter the password you want to store: ")
            password_storage(password, Service)
            application_home()
        elif choice == '3':
            try:
                with open("passwords.txt", "r") as file:
                    passwords = file.readlines()
                    if passwords:
                        print("Stored Passwords:")
                        for line in passwords:
                            print(line.strip())
                    else:
                        print("No passwords stored yet.")
            except FileNotFoundError:
                print("No passwords stored yet.")
            application_home()
        elif choice == '4':
            print("Exiting the Password Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
    print("Thank you for using the Password Manager!")


def ask_command():
    #get the number of characters for the password
    print('How many characters do you want in your password..')
    while True:
        length = input("Enter password length (8-32): ")
        if length.isdigit():            #check if input is a digit
            length = int(length)
            if 8 <= length <= 32:       #check if length is within the valid range
                print(f'The length of your password is {length}')
                break
            else:
                print("Your password length is either too short or too long. Try again")
        else:
            print("Enter a valid number.")
    
    print('Generating the password........')
    password = generate_password(length)
    print(f'Your password is: {password}')


def generate_password(length):
    # Define the characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation
    # Randomly choose 'length' characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

application_home()

