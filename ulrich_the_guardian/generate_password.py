import secrets
import string
import random
def generate():
    random_range= random.randint(8,32)
    print("Lenght:", random_range)
    password = ''.join((secrets.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(random_range)))
    print(password)
