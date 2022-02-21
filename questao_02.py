def validate_password(password: str) -> int:
    """
    It has at least 6 characters.
    Contains at least 1 digit.
    Contains at least 1 lowercase letter.
    Contains at least 1 capital letter.
    Contains at least 1 special character
    :param password:
    :return: how many characters are left for the password to be secure
    """
    count = 0
    special = '!@#$%^&*()-+'
    numbers = '0123456789'
    intersection_special = set(password).intersection(set(special))
    intersection_number = set(password).intersection(set(numbers))
    has_uppercase = password != password.lower()
    has_lowercase = password != password.upper()
    password_size = len(password)
    diff_size = 6 - password_size

    if not intersection_special:
        count += 1
    if not intersection_number:
        count += 1
    if not has_lowercase:
        count += 1
    if not has_uppercase:
        count += 1

    if password_size >= 6:
        return count
    elif diff_size > count:
        return diff_size
    else:
        return count


