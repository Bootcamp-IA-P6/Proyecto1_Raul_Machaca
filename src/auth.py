from config import USERNAME, PASSWORD

def authenticate(user, pwd):
    return user == USERNAME and pwd == PASSWORD
