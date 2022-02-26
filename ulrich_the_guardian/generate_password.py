from tinydb import TinyDB, Query
def generate():
    print("TOTO")
    db = TinyDB('./data/db.json')
    db.insert({'type': 'apple'})
