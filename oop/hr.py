class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def get_salary(self):
        return self._salary

    def get_name(self):
        return self._name.upper()

    def __str__(self):
        return "%s %d" % (self._name, self._salary)


class Manager(Employee):
    def __init__(self, name, salary, hra):
        super().__init__(name, salary)
        self._hra = hra

    # Overriding get_salary() of super class
    def get_salary(self):
        return super().get_salary() + self._hra

    def __str__(self):
        return "%s %d %d" % (self._name, self._salary, self._hra)


e = Employee("Mr. Bean",50000)
print(e.get_name())
print(e.get_salary())

m = Manager("Mr. Bill",100000,20000)
print(m.get_name())
print(m.get_salary())

print( isinstance(m,Employee))
print( isinstance(e,Employee))
print( isinstance(e,Manager))
print( issubclass(Manager,object))

print (type(m))




