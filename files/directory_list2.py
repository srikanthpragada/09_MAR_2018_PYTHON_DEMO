# open file for writing in text mode
phones = dict()
with open(r"e:\classroom\python\mar9\phones.txt", "rt") as f:
    for line in f.readlines():
        parts = line.split(',')
        if len(parts) < 2:
            continue

        name = parts[0]
        phone = parts[1].strip("\n")
        # Name is existing in dict
        if name in phones:
            phones[name].add(phone)  # add phone to existing set
        else:
            phones_set = set()
            phones_set.add(phone)
            phones[name] = phones_set  # create new entry in dict

for name, value in sorted(phones.items()):
    print("%-10s" % (name), end=' ' * 3)
    for p in value:
        print("%-10s" % (p), end=' ' * 2)

    print()  # Go to next line
