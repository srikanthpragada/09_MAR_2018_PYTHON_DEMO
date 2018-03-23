class Time:
    @classmethod
    def create(cls):
        return cls(10,20,30)

    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s

    def __str__(self):
        return "%02d:%02d:%02d" % (self.h, self.m, self.s)


# create an object
t = Time.create()
print(t)  # calls str(t) ->  t.__str__()
