import sqlite3

try:
    con = sqlite3.connect(r"e:\classroom\python\hr.db")
    print("Connected To Sqlite")
except Exception as ex:
    print("Could not connect to database. Error : ", ex)
else:
    con.close()





