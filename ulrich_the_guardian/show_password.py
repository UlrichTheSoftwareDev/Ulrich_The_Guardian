from tinydb import TinyDB, Query
import getpass
import sys
import hashlib
import random
import string
import base64
from Crypto.Cipher import AES

def show_password_db():
    db = TinyDB('./data/db.json')
    val = input("Password ID: ")
    User = Query()
    print(bool(db.get(doc_id=44)))


#    toto = db.get(User.doc_id == "1")
#    print(toto)
#    a = toto.get("key")
#    b = toto.get("iv")
#    c = toto.get("message")
#    print(a, type(a), len(a))
#    print(c, type(c), len(c))
#    a = a[2:]
#    a = a[:-1]
#    b = b[2:]
#    b = b[:-1]
#    a_enc = a.encode()
#    b_enc = b.encode()
#    c = c[2:]
#    c = c[:-1]
#    print(a_enc)
#    print(b_enc)
#    print(c)
#    decryption_suite = AES.new(a_enc, AES.MODE_CFB,b_enc)
#    plain_text = decryption_suite.decrypt(base64.b64decode(c))
#    print(plain_text)
