from tinydb import TinyDB, Query
import getpass
import sys
import hashlib
import random
import string
import base64
from Crypto.Cipher import AES

def add_password_db():
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

        hashed_string = hashlib.sha256(val.encode('utf-8')).hexdigest()
        hashed_string_enc = hashed_string[0:32].encode()

        iv = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(16))
        iv_enc = iv.encode()

        enc_s = AES.new(hashed_string_enc, AES.MODE_CFB, iv_enc)

        cipher_text = enc_s.encrypt(message_enc)
        encoded_cipher_text = base64.b64encode(cipher_text)
        db = TinyDB('./data/db.json')
        db.insert({'key': str(hashed_string_enc), 'iv': str(iv_enc), 'message': str(encoded_cipher_text)})

    ##    User = Query()
    ##    toto =db.get(User.message == "b'oTje6xMc+QxnEr/Ohw=='")
    ##    a = toto.get("key")
    ##    b = toto.get("iv")
    ##    c = toto.get("message")
    ##    print(a, type(a), len(a))
    ##    print(c, type(c), len(c))
    ##    a = a[2:]
    ##    a = a[:-1]
    ##    b = b[2:]
    ##    b = b[:-1]
    ##    a_enc = a.encode()
    ##    b_enc = b.encode()
    ##    c = c[2:]
    ##    c = c[:-1]
    ##    print(a_enc)
    ##    print(b_enc)
    ##    print(c)




    #    decryption_suite = AES.new(hashed_string_enc, AES.MODE_CFB,iv_enc)
    #    plain_text = decryption_suite.decrypt(base64.b64decode(encoded_cipher_text))
    #    print(plain_text)
    ##    decryption_suite = AES.new(a_enc, AES.MODE_CFB,b_enc)
    ##    plain_text = decryption_suite.decrypt(base64.b64decode(c))
    ##    print(plain_text)
    #db = TinyDB('./data/db.json')
    #db.insert({'type': 'apple'})
