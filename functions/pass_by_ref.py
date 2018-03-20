def add(list, item):
    print(id(list))
    list.append(item)


names = []
print(id(names))
add(names, "Bill")
add(names, "Jeff")
print(names)
