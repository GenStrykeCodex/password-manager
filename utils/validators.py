# Check if a string is empty or not
def is_non_empty_string(value: str) -> bool:
    return isinstance(value, str) and bool(value.strip())


# Check if the given service name is valid or not
def validate_service_name(service: str) -> bool:
    return is_non_empty_string(service)


# Check if the given name is a valid name or not
def validate_username(username: str) -> bool:
    return is_non_empty_string(username)


# Check if value can be safely converted to int.
def validate_integer(value: str) -> bool:
    return value.isdigit()
