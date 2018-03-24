
class Test:
    pass


t = Test()
t.name  = "Test"
t.phone = "393934343"
t.__dict__["email"] = "abc@bbc.com"

print(t.__dict__)

for k in t.__dict__.keys():
    print(k)