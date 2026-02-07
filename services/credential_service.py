from models.credential import Credential
from services.storage_service import load_credentials, save_credentials
from utils.validators import validate_service_name, validate_username


# Add a credential detail.
def add_credential(service: str, username: str, password: str) -> None:
    if not validate_service_name(service):
        raise ValueError("Service name cannot be empty.")

    if not validate_username(username):
        raise ValueError("Username cannot be empty.")

    credentials = load_credentials()

    service_key = service.lower().strip()
    if service_key in credentials:
        raise ValueError(f"Credential for '{service}' already exists.")

    credential = Credential(
        service=service_key,
        username=username,
        password=password
    )

    credentials[service_key] = credential
    save_credentials(credentials)


# Return all stored credentials.
def get_all_credentials() -> dict[str, Credential]:
    return load_credentials()


# Fetch a single credential by service name.
def get_credential(service: str) -> Credential | None:
    credentials = load_credentials()
    return credentials.get(service.lower().strip())


# Update username and/or password for a credential.
def update_credential(service: str, username: str | None = None, password: str | None = None) -> None:
    credentials = load_credentials()
    service_key = service.lower().strip()

    if service_key not in credentials:
        raise ValueError(f"No credential found for '{service}'.")

    credential = credentials[service_key]

    if username:
        if not validate_username(username):
            raise ValueError("Invalid username.")
        credential.username = username.strip()

    if password:
        credential.password = password

    save_credentials(credentials)


# Delete a stored credential.
def delete_credential(service: str) -> None:
    credentials = load_credentials()
    service_key = service.lower().strip()

    if service_key not in credentials:
        raise ValueError(f"No credential found for '{service}'.")

    del credentials[service_key]
    save_credentials(credentials)
