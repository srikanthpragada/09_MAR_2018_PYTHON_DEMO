import sqlite3

try:
    con = sqlite3.connect(r"e:\classroom\python\hr.db")
    cur = con.cursor()
    cur.execute("select empid, empname, salary, salary * .40, name from emp join dept on (emp.deptid = dept.id)")
    for row in cur.fetchall():
        print("%4d %-20s %5d %5d %-20s" % (row))

    cur.close()
except Exception as ex:
    print("Error : ", ex)
finally:
    con.close()





