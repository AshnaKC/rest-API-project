import sqlite3
import json
DB ="SqliteDBtest.db"
def get_all_users(json_str = False):
    conn =sqlite3.connect( DB )
    conn.row_factory =sqlite3.Row
    db= conn.cursor()
    rows =db.execute("select * from tbl_userinfo").fetchall()
    conn.commit()
    conn.close()
    if json_str:
        return json.dumps([dict(ix) for ix in rows])
    return rows
print (get_all_users(json_str= True))