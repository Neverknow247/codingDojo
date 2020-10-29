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

nathan = User("Nathan")
print (nathan.name)

nathan.make_deposit(300)
print(nathan.balance)
nathan.make_withdrawal(50)
print(nathan.balance)

rob = User("Rob")

nathan.transfer_money(rob, 100)
print(nathan.balance)
print(rob.balance)



