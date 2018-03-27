class InsufficientBalanceError(Exception):
    def __init__(self, balance, amount):
        self.message = "Insufficient Balance %d. Widthdraw amount id %d." % (balance, amount)

    def __str__(self):
        return self.message


class Account:
    # class attribute
    count = 0
    minbal = 10000

    def __init__(self, acno, customer, balance=0):
        self.__acno = acno
        self.__customer = customer
        self.__balance = balance
        Account.count += 1

    def __del__(self):
        Account.count -= 1

    def print(self):
        print("Account no: ", self.__acno)
        print("Customer name: ", self.__customer)
        print("Account balance: ", self.__balance)

    def __str__(self):
        return "{0} {1} {2}".format(self.__acno, self.__customer, self.__balance)

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance - Account.minbal >= amount:
            self.__balance -= amount
        else:
            raise InsufficientBalanceError(self.__balance, amount)

    def __eq__(self, other):
        return self.__acno == other.__acno

    @staticmethod  # Decorator
    def set_minbal(newminbal):
        Account.minbal = newminbal


c1 = Account(123456, "Guido", 15000)

try:
    c1.withdraw(50000)
    print("Withdrew")
except Exception as ex:
    print("Error : ", ex)
