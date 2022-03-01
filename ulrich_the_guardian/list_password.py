from tinydb import TinyDB, Query

def list_password_db():
    """List all lines from DB """
    db = TinyDB('./data/db.json')
    for item in db:
        print(item.doc_id, item)
