from tinydb import TinyDB, Query
import getpass
import sys
import base64
import hashlib
from Crypto.Cipher import AES

def show_password_db():
    """Decrypt password from DB: get message from doc_id"""
    db = TinyDB('./data/db.json')
    val = input("Password ID: ")
    key = getpass.getpass("Key:")
    User = Query()
    val_bool = bool(db.get(doc_id=val))
    if val_bool == True:
        val_result = db.get(doc_id=val)

        val_key = hashlib.sha256(key.encode('utf-8')).hexdigest()
        val_iv = val_result.get("iv")
        val_message = val_result.get("message")

        val_iv = val_iv[2:]
        val_iv = val_iv[:-1]
        val_message = val_message[2:]
        val_message = val_message[:-1]

        val_key_enc = val_key[0:32].encode()
        val_iv_enc = val_iv.encode()

        decryption_suite = AES.new(val_key_enc, AES.MODE_CFB,val_iv_enc)
        plain_text = decryption_suite.decrypt(base64.b64decode(val_message))
        print(plain_text)
    else:
        sys.exit("Password does not exist !")
