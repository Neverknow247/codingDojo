class User:
    def __init__(self,name):
        self.name = name
        self.email = "email"
        self.balance = 0
    def make_deposit(self, amount):
        self.balance += amount
        return self
    def make_withdrawal(self, amount):
        self.balance -= amount
        return self
    def transfer_money(self, other, amount):
        self.balance -= amount
        other.balance += amount
        return self
    def displayBalance(self):
        print(f"User: {self.name}, Balance: ${self.balance}")
        return self

nathan = User("Nathan")
nathan.make_deposit(300).make_deposit(100).make_deposit(50).make_withdrawal(150).displayBalance()

rob = User("Rob")
rob.make_deposit(25.50).make_deposit(25000).make_withdrawal(1.99).make_withdrawal(.69).displayBalance()

nathan.transfer_money(rob, 100).displayBalance()
rob.displayBalance()

aaron = User("Aaron")
aaron.make_deposit(5).make_withdrawal(1).make_withdrawal(2).make_withdrawal(1.25).displayBalance()


