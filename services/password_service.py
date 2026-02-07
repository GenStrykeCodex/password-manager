import random
import string

MIN_LENGTH = 8
MAX_LENGTH = 32


# Generate a random password of given length
def generate_password(length: int = 8) -> str:
    if not is_valid_length(length):
        raise ValueError(f"Password length must be between {MIN_LENGTH} and {MAX_LENGTH}")

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""
    for i in range(length):
        password += random.choice(characters)

    return password


# Validate the length of password
def is_valid_length(length: int) -> bool:
    return (
        MIN_LENGTH <= length <= MAX_LENGTH
    )
