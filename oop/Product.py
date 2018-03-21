class Product:
    def __init__(self, name, price=None):
        # instance variables
        self.__name = name
        self.__price = price

    def print(self):
        print('Name ', self.__name)
        print("Price ", self.__price)

    def __str__(self):
        # return "%s %d" % (self.__name, self.__price)
        return "{0} {1}".format(self.__name, self.__price)

    def __eq__(self, other):
        return self.__name == other.__name

#    def __gt__(self, o):
#        return self.__price > o.__price


p1 = Product("iPhone X", 70000)
print(str(p1))

p2 = Product("iPhone 8", 60000)
print(p1 != p2)  # calls __eq__ and negates

print(p1 < p2)  # __gt__(p1,p2)
