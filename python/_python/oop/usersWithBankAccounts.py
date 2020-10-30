
class BankAccount:
    def __init__(self, int_rate, balance):
        self.interest_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.interest_rate
            self.balance = round(self.balance*100)/100
        return self

    def transfer_money(self, other, amount):
        self.balance -= amount
        other.balance += amount

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def newAccount(self,int_rate,balance):
        return BankAccount(int_rate,balance)

nathan = User("Nathan","nate@gmail.com")
nathan.savings = nathan.newAccount(0.05,100)
nathan.savings.deposit(200).yield_interest().display_account_info()

rob = User("Nathan","nate@gmail.com")
rob.savings = rob.newAccount(0.05,1000)
rob.savings.deposit(20).yield_interest().display_account_info()

nathan.savings.transfer_money(rob.savings, 315)
nathan.savings.display_account_info()
rob.savings.display_account_info()
