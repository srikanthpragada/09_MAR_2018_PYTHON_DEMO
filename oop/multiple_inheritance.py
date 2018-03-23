class Base1:
    def fun1(self,name):
        self.name = name
        print("fun1() in Base1", self.name)


class Base2:
    def fun2(self,email):
        self.email = email
        print("fun2() in Base2", self.email)


class Derived(Base1, Base2):
    def __init__(self,name, email):
        super().__init__(name)




d = Derived("Abc","abc@gmail.com")
d.fun1()
d.fun2()
