from services.credential_service import (
    add_credential,
    get_all_credentials,
    get_credential,
    update_credential,
    delete_credential
)

from services.password_service import generate_password
from utils.validators import validate_integer

MAIN_MENU_LENGTH = 7

print("Welcome to Password Manager v2.0.0!")


''' Helper Functions '''

# Create pauses between actions
def pause():
    input("\nPress Enter to return")


# Get menu choice from user
def get_choice(num):
    while True:
        try:
            choice = int(input(f"\nChoose an option (1-{num}): "))
            return choice

        except ValueError:
            print("Sorry! That's not an valid option.")


''' Menu Display Functions '''


# Main Menu of the application
def main_menu():
    print("\n──────────────────────────")
    print("     Password Manager     ")
    print("──────────────────────────")
    print("1. Generate Password")
    print("2. Add Credential")
    print("3. View All Credentials")
    print("4. Search a Credential")
    print("5. Update Credential")
    print("6. Delete Credential")
    print("7. Exit")
    print("──────────────────────────")


# UI Handler functions
def handle_generate_password():
    length_input = input("Enter password length (8-32): ").strip()

    if not validate_integer(length_input):
        print("Invalid input. Please enter a number.")
        return

    try:
        password = generate_password(int(length_input))
        print(f"Generated Password: {password}")

        while True:
            store = input("Do you want to store this password? (y/n): ").lower().strip()

            if store == "y":
                handle_add_credential(password)
                return
            elif store == "n":
                return
            else:
                print("Please enter a valid choice.")

    except ValueError as e:
        print(e)


def handle_add_credential(password: str | None):
    service = input("Enter the Service name: ").strip()
    username = input("Enter your Username / Email: ").strip()

    if not password:
        password = input("Enter your Password: ")

    try:
        add_credential(service, username, password)
        print("Credential added successfully.")
    except ValueError as e:
        print(e)


def handle_view_all_credentials():
    credentials = get_all_credentials()

    if not credentials:
        print("No credentials stored.")
        return

    print("\nStored Credentials:")
    print("\n" + "─" * 83)
    print(f"{'#':<3} | {'Service':<15} | {'Username':<30} | {'Password':<35}")
    print("─" * 83)
    for i, (service, credential) in enumerate(credentials.items()):
        print(f"{i + 1:<3} | {service:<15} | {credential.username:<30} | {credential.password:<35}")
    print("─" * 83)


def handle_view_single_credential():
    service = input("Enter service name: ").strip()
    credential = get_credential(service)

    if not credential:
        print("Credential not found.")
        return

    print("\nCredential Details:")
    print(f"Service  : {credential.service}")
    print(f"Username : {credential.username}")
    print(f"Password : {credential.password}")
    print(f"Created  : {credential.created_at}")


def handle_update_credential():
    service = input("Enter service name to update: ").strip()
    username = input("New username (leave blank to skip): ").strip()
    password = input("New password (leave blank to skip): ")

    try:
        update_credential(
            service,
            username=username if username else None,
            password=password if password else None
        )
        print("Credential updated successfully.")
    except ValueError as e:
        print(e)


def handle_delete_credential():
    service = input("Enter service name to delete: ").strip()

    try:
        delete_credential(service)
        print("Credential deleted successfully.")
    except ValueError as e:
        print(e)


# Main Loop of the application
def main():
    while True:
        main_menu()

        while True:
            choice = get_choice(MAIN_MENU_LENGTH)

            if choice == 1:
                handle_generate_password()
                pause()
                break
            elif choice == 2:
                handle_add_credential(None)
                pause()
                break

            elif choice == 3:
                handle_view_all_credentials()
                pause()
                break

            elif choice == 4:
                handle_view_single_credential()
                pause()
                break

            elif choice == 5:
                handle_update_credential()
                pause()
                break

            elif choice == 6:
                handle_delete_credential()
                pause()
                break

            elif choice == 7:
                print("Closing the application..")
                return

            else:
                print("Sorry! This choice is out of range.")


if __name__ == "__main__":
    main()

print("\nThank you for using our application!")