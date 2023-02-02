import sqlite3
con = sqlite3.connect("./sqlite/database/sensor.db")

cur = con.cursor()
cur.execute("SELECT * FROM sensor")