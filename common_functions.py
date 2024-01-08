from config import SALT

def salt(password):
    return SALT.format(password)