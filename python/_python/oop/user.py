# make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
# display_user_balance(self) - have this method print the user's name and account balance to the terminal
# eg. "User: Guido van Rossum, Balance: $150
# BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance


class User:
    def __init__(self,name):
        self.name = name
        self.email = "email"
        self.balance = 0
    def make_deposit(self, amount):
        self.balance += amount
    def make_withdrawal(self, amount):
        self.balance -= amount
    def transfer_money(self, other, amount):
        self.balance -= amount
        other.balance += amount
    def displayBalance(self):
        print(f"User: {self.name}, Balance: ${self.balance}")

nathan = User("Nathan")
nathan.make_deposit(300)
nathan.make_deposit(100)
nathan.make_deposit(50)
nathan.make_withdrawal(150)
nathan.displayBalance()

rob = User("Rob")
rob.make_deposit(25.50)
rob.make_deposit(25000)
rob.make_withdrawal(1.99)
rob.make_withdrawal(.69)
rob.displayBalance()

nathan.transfer_money(rob, 100)
nathan.displayBalance()
rob.displayBalance()

aaron = User("Aaron")
aaron.make_deposit(5)
aaron.make_withdrawal(1)
aaron.make_withdrawal(2)
aaron.make_withdrawal(1.25)
aaron.displayBalance()


