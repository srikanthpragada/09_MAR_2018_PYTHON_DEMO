from threading import Thread


class PrimeThread(Thread):
    def __init__(self, num):
        super().__init__();
        self.num = num

    def run(self):
        for i in range(2, self.num // 2 + 1):
            if self.num % i == 0:
                print(self.num, " is not prime because it is divisble by ", i)
                break
        else:
            print(self.num, " is prime")


nums = [1019212121, 19, 29,223827329831, 87237299, 2838383, 1121211]

for n in nums:
    t = PrimeThread(n)
    t.start()
