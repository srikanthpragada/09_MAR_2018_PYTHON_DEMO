a = 10 # Global scope


def f1():
    a = 20  # Enclosing

    def f2():
        # a = 30  # Local
        print(a)

    f2()


f1()
