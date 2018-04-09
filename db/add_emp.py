import sqlite3

try:
    con = sqlite3.connect(r"e:\classroom\python\hr.db")
    cur = con.cursor()
    # take input from user
    ename = input("Enter name  :")
    salary = input("Enter salary : ")
    dept = input("Enter dept id :")
    # get next emp id
    cur.execute("select max(empid) + 1 from emp")
    empid = cur.fetchone()[0]
    cur.execute("insert into emp values(?,?,?,?)", (empid, ename, salary, dept))
    con.commit()
    print("Added Employee")
except Exception as ex:
    print("Error : ", ex)
finally:
    con.close()
