t1 = (1, "Abc", False)

for v in t1:
    print(v)

print(t1)
print(t1[0])
t2 = (10,)

print(type(t2))

v1, v2, v3 = t1  # Unpacking

print(v1)
print(v2)
print(v3)

nt = ((10, 20), (1, 2, 3))

print(nt[1])

person = ("Srikanth", ["Java", "Python"])
person[1].append("C#")   # List is mutable so can be modified

print(person[0])
print(person[1])

s1 = set(t1)
print(s1)
