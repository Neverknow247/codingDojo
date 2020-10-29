

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


savings = BankAccount(.05, 200)
checking = BankAccount(.02, 300)

savings.deposit(20).deposit(100).deposit(1400).withdraw(200).yield_interest().display_account_info()
checking.deposit(200).deposit(900).withdraw(14.07).withdraw(56).withdraw(10).withdraw(300).yield_interest().display_account_info()
