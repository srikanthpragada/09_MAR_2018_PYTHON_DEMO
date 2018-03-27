class MyTime:
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s

    def __str__(self):
        return "%02d:%02d:%02d" % (self.h, self.m, self.s)

    @property
    def total_seconds(self):
        return self.h * 3600 + self.m * 60 + self.s

    def __eq__(self, other):
        return self.total_seconds == other.total_seconds

    def __gt__(self, other):
        return self.total_seconds > other.total_seconds

    def __iadd__(self, other):
        if not isinstance(other, int):
            return self

        self.s += other
        if self.s > 59:
            self.s = self.s % 60
            self.m += 1
            if self.m > 59:
                self.m = 0
                self.h += 1

        return self


t1 = MyTime(1, 2, 3)
t2 = MyTime(1, 2, 3)

print(t1 > t2)
t1 += 5
t1 += "abc"

print(t1)
