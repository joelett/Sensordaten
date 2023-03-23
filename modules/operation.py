import os
from datetime import date
import csv, sqlite3
import pandas as pd

csv_files = "./sqlite/database/sensor_data/"

con = sqlite3.connect("./sqlite/database/database.db") # change to 'sqlite:///your_filename.db'
cur = con.cursor()
#cur.execute("CREATE TABLE t (col1, col2);") # use your column names here

def initialize():
    cur.execute("CREATE TABLE IF NOT EXIST Entries (sensor_id INT,sensor_type TEXT,location INT,lat REAL,lon REAL,timestamp TEXT,P1 REAL,durP1 REAL,ratioP1 REAL,P2 REAL,durP2 REAL,ratioP2 REAL)")
    for path in os.listdir(csv_files):
        if os.path.isfile(os.path.join(csv_files, path)):
            users = pd.read_csv(path)
            users.to_sql('users', con, if_exists='append', index = False)
            print(path)

def test(results):
    print(results)

initialize()