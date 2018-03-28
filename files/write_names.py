# open file for writing in text mode
try:
    with open(r"e:\classroom\pytho\mar9\names.txt", "wt") as f:
        names = ["Python", "C#", "Java", "JavaScript", "C++"]
        for name in sorted(names):
            f.write(name + "\n")
except Exception as ex:
    print("Error :", ex)


