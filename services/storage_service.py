from utils.file_handler import load_json, save_json
from models.credential import Credential

PASSWORDS_FILE = "passwords.json"


def load_credentials() -> dict[str, Credential]:
    """
    Load credentials from JSON storage and return them
    as a dictionary of Credential objects.
    """
    raw_data = load_json(PASSWORDS_FILE, default={})

    credentials: dict[str, Credential] = {}

    for service, credential_data in raw_data.items():
        try:
            credentials[service] = Credential.from_dict(credential_data)
        except Exception:
            # Skip malformed entries instead of crashing
            continue

    return credentials


# Save credentials to JSON storage.
def save_credentials(credentials: dict[str, Credential]) -> None:
    data: dict[str, dict] = {}

    for service, credential in credentials.items():
        data[service] = credential.to_dict()

    save_json(PASSWORDS_FILE, data)
