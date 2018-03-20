def change(n):
    print("Address of n ", id(n))
    n = 0
    print("Address of n after change ", id(n))


v = 10
print("Address of v ", id(v))
change(v)
print(v)


