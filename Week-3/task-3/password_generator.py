import random
import string

def generate_password(length=12):
    if length < 6:
        return "Password too short!"

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
