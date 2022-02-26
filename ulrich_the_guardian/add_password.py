from tinydb import TinyDB, Query
import getpass
import sys

def add_password_db():
    const_lenght = 8
    val = getpass.getpass('Enter your password:')
    if len(val) < const_lenght:
        sys.exit("ERROR: your password must be greater than 8 characters !")
    else:
        print("toto")
    #db = TinyDB('./data/db.json')
    #db.insert({'type': 'apple'})
