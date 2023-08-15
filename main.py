class BankAccount:
    def __init__(self, balance=0, interest_rate=0.01):
        self.balance = balance
        self.interest_rate = interest_rate

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}")
        else:
            print("Invalid deposit amount")
        return self

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}")
        else:
            print("Insufficient funds: charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance ${self.balance:.2f}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            interest_amount = self.balance * self.interest_rate
            self.balance += interest_amount
            print(f"Interest added: ${interest_amount:.2f}")
        else:
            print("No interest added, balance is not positive")
        return self


# Print information for all instances of BankAccount
def print_all_accounts_info():
    for obj in globals().values():
        if isinstance(obj, BankAccount):
            obj.display_account_info()


# Creating instances of BankAccount
account1 = BankAccount(1000, 0.02)  # Starting balance is $1000, & the interest rate is 2%
account2 = BankAccount()  # Default balance $0, and the default interest rate is 1%

# Chaining operations on account1
account1.deposit(500).deposit(200).deposit(300).withdraw(400).yield_interest().display_account_info()

# Chaining operations on account2
account2.deposit(100).deposit(150).withdraw(50).withdraw(30).withdraw(20).withdraw(
    10).yield_interest().display_account_info()

# print all the accounts' info
print_all_accounts_info()
