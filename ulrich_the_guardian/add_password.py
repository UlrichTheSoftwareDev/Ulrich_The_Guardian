from tinydb import TinyDB, Query
import getpass
import sys
import hashlib
import random
import string
import base64
from datetime import date
from Crypto.Cipher import AES

def add_password_db():
    """Add password in DB: minimum lenght 8 char -> no complexity needed, 16 bytes IV and 32 bytes key AES 256 CFB"""
    const_lenght = 8
    val = getpass.getpass('Enter your password:')
    if len(val) < const_lenght:
        sys.exit("ERROR: your password must be greater than 8 characters !")
    else:
        message = getpass.getpass("Password to encrypt:")
        message_enc = message.encode()

        message_con = getpass.getpass("Retype:")

        if message != message_con:
            sys.exit("ERROR: password does not match !")

        email = input("Email:")
        comment = input("Comment:")
        today = date.today()
        date_now = today.strftime("%d/%m/%Y")

        hashed_string = hashlib.sha256(val.encode('utf-8')).hexdigest()
        hashed_string_enc = hashed_string[0:32].encode()

        iv = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(16))
        iv_enc = iv.encode()

        enc_s = AES.new(hashed_string_enc, AES.MODE_CFB, iv_enc)

        cipher_text = enc_s.encrypt(message_enc)
        encoded_cipher_text = base64.b64encode(cipher_text)

        db = TinyDB('./data/db.json')
        db.insert({'Date': str(date_now), 'Email': str(email), 'IV': str(iv_enc), 'Password': str(encoded_cipher_text), 'Comment': str(comment)})
