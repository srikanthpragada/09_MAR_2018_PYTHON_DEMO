try:
    print("Try")
    v = int("Abc")
    a = 10 / 0
except (ZeroDivisionError, StopIteration) as ex:
    print("Error :", ex)
except Exception as ex:
    print("Common Error :", ex)
else:
    print("Else")
finally:
    print("finally")

print("The End")
