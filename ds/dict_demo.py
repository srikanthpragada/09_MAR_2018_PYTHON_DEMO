emails={}
phones = {"Bill": "3939393", "Joe": "393939332"}
print(phones["Bill"])
phones["Jack"] = "391911212"
phones["Jason"] = "999999999"

for name in phones.keys():
    print(name)

for name in sorted(phones.keys()):
    print(name, phones[name])

for name, phone in phones.items():
    print(name, phone)

if "Steve" in phones:
    print(phones["Steve"])
else:
    print("Sorry! Steve Not Found!")

print(phones.get("Abc","99999999"))

print (type(phones.items()))

