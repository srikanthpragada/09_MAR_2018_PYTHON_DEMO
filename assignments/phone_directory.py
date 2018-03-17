phones = {}
while True:
    name = input("Enter name :")
    if name == "end":
        break

    mobile = input("Enter mobile number :")

    if name in phones:  # name is found
        phones[name].add(mobile)   # add new number to existing set
    else:
        phones[name] = {mobile}   # Add a new entry with name and set

# print directory

for name, numbers in phones.items():
    print(name, numbers)
