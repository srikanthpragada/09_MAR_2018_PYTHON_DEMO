# open file for writing in text mode
import re

phones = dict()
with open(r"e:\classroom\python\mar9\phones.txt", "rt") as f:
    for line in f.readlines():
        parts = line.split(",")

        if len(parts) < 2:
            continue

        name = parts[0]
        mobile = parts[1].strip('\n')
        # print(name,mobile)
        # validate name
        if not re.fullmatch(r'[a-zA-Z ]+', name):
            continue;
        # validate mobile number
        if not re.fullmatch(r'\d{10}',mobile):
            continue;

        phones[parts[0]] = parts[1].strip('\n')

for name, value in sorted(phones.items()):
    print(name, value)
