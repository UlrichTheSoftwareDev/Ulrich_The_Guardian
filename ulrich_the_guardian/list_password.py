from tinydb import TinyDB, Query

def list_password_db():
    db = TinyDB('./data/db.json')
    for item in db:
        print(item.doc_id, item)
