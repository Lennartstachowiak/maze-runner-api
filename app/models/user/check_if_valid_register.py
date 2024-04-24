import re


def is_valid_email(email):
    email_regex = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    return re.match(email_regex, email)


def is_valid_password(password):
    # Regular expression pattern for password validation
    password_regex = r"^(?=.*[a-zA-Z])(?=.*\d)(?=.*[@$!%*?&])[a-zA-Z\d@$!%*?&]{8,}$"
    return re.match(password_regex, password)


def check_if_valid_register(email, password, repeated_password):
    if not is_valid_email(email):
        return False
    if not is_valid_password(password):
        return False
    if password != repeated_password:
        return False
    return True
