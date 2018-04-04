from datetime import *

sd = date(2018, 1, 1)
print(sd)

cd = date.today()
print(cd)

td = cd - sd
print(td.days, td.seconds)

nd = cd + timedelta(days=10)
print(nd)
try:
    s = "20180401 10:20"
    ed = datetime.strptime(s, "%Y%m%d %H:%M")
    print(ed)
except:
    print("Invalid date")

ct = datetime.now()
print(ct.strftime("%d/%m/%Y %H:%M"))

d1 = date(2018,1,1)
d2 = date(2018,2,2)

print(d2 < d1)

