unames = set()
dnames = set()

while True:
    name = input("Enter name :")
    if name == "end":
        break

    if name in unames:
        dnames.add(name)  # add to duplicate names
    else:
        unames.add(name)  # add to unique names

print("Unqiue Names")
for n in unames:
    print(n)

print("Duplicate Names")
for n in dnames:
    print(n)
