from tinydb import TinyDB, Query

def remove_password_db():
    """Remove password from DB: get doc_id then delete if match """
    db = TinyDB('./data/db.json')
    val = input("Delete saved password: ")
    val_int = int(val)
    for item in db:
        if item.doc_id == val_int:
            db.remove(doc_ids=[val_int])
