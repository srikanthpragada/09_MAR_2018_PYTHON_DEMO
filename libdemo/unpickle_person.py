import pickle
from person import Person

f = open("person.dat", "rb")
p = pickle.load(f)  # unpickle object
f.close()
print(str(p))
