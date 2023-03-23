import sqlite3
con = sqlite3.connect("./sqlite/database/database.db")

cur = con.cursor()
#cur.execute("SELECT * FROM sensor")

def execute(query,params,callback):
    exe = cur.execute(query,params)
    callback(exe.fetchall())