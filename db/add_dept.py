import sqlite3

try:
    con = sqlite3.connect(r"e:\classroom\python\hr.db")
    cur = con.cursor()
    # take input from user
    id = input("Enter dept id :")
    name =input ("Enter dept name : ")
    cur.execute("insert into dept values(?,?)", (id,name))
    con.commit()
    print("Added Dept")
except Exception as ex:
    print("Error : ", ex)
finally:
    con.close()





