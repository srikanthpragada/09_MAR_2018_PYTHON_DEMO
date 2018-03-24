class Base1():
    def fun(self):
        print("fun() in Base1")

class Base2():
    def fun(self):
        print("fun() in Base2")

class Derived(Base1, Base2):
    def fun(self):
        Base1.fun(self)
        Base2.fun(self)
        print("fun() in Derived")

d = Derived()
d.fun()





