class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def moneyX(self):
        money = int(input('Money to add: '))
        self._balance += money

    def _kill(self):
        self._balance = 0

    def __jackpot(self):
        self._balance *= 10

    def _merge(self, another_balance):
        self._balance += another_balance

print(dir(Bank))
b1 = Bank('Temirlan', 1000)
b1.moneyX()
print(b1._balance)
b1._Bank__jackpot()
print(b1._balance)
b1._kill()
print(b1._balance)
b2 = Bank('Random', 12000)
b1._merge(b2._balance)
print(b1._balance)

