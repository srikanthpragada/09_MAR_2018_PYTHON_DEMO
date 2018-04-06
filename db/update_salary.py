import sqlite3
try:
    con = sqlite3.connect(r"e:\classroom\python\hr.db")
    cur = con.cursor()
    # take input from user
    id = input("Enter employee id :")
    salary =input ("Enter new salary : ")
    cur.execute("update emp set salary = ? where empid  = ?", (salary,id))
    if cur.rowcount == 1:
        print("Updated Salary!")
        con.commit()
    else:
        print("Sorry! Employee not found!")

    cur.close()
except Exception as ex:
    print("Error : ", ex)
finally:
    con.close()





