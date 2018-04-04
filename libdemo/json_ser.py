import json
from person import Person


p1 = Person("Srikanth","srikanthpragada@yahoo.com")
d1 = {"name" : p1.name, "email" : p1.email}
d2 = {"name" : "Jason", "email" : "jason@gmail.com"}

print(json.dumps(d1))

person = [d1,d2]
print(json.dumps(person))

