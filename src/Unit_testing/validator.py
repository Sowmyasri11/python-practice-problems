import re

from .exceptions import InvalidEmailError,InvalidPhoneError


def validate_email(email):
    pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        raise InvalidEmailError("Invalid email format")
    return True


def validate_phone(phone):
    pattern = r'^[6-9]+\d{9}$'
    if not re.match(pattern, phone):
        raise InvalidPhoneError("Invalid phone number")
    return True
