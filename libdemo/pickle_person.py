import pickle
from person import Person


f = open("person.dat","wb")
p1 = Person("Srikanth","srikanthpragada@yahoo.com")
pickle.dump(p1,f) #pickle object
print("Dumped object to file!")
f.close()