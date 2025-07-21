import string
import random

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

ask_command()

