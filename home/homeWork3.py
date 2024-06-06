class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def moneyX(self):
        money = int(input('Money to add: '))
        self.balance += money

    def _kill(self):
        self.balance = 0

    def __jackpot(self):
        self.balance *= 10

    def _merge(self, another_balance):
        self.balance += another_balance


b1 = Bank('Temirlan', 1000)
b1.moneyX()
print(b1.balance)
b1._Bank__jackpot()
print(b1.balance)
b1._kill()
print(b1.balance)
b2 = Bank('Random', 12000)
b1._merge(b2.balance)
print(b1.balance)

