import sqlite3

def get_db():
    return sqlite3.connect("../data/receipts.db")



def add_task(data: dict):
   conn = get_db()

    conn.execute("")    


   conn.close()
