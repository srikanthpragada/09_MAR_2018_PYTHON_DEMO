class Test:
    def fun(self, x=0,y=0):
        print('First fun')


v = Test()
v.fun(y=30)
print( Test.__dict__)



