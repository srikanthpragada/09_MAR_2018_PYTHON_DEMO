# open file for writing in text mode
phones = dict()
with open(r"e:\classroom\python\mar9\phones.txt", "rt") as f:
    for line in f.readlines():
        parts = line.split(',')
        if len(parts) < 2:
            continue
        phones[parts[0]] = parts[1].strip('\n')

for name, value in sorted(phones.items()):
    print(name, value)
