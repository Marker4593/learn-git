class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount
    
    def display_balance(self):
        print(f"Account Balance: {self.balance}")

class SavingAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate
    
    def apply_interest(self):
        calcu_interest_rate = (self.balance / 100) * self.interest_rate
        self.balance += calcu_interest_rate

class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance, transaction_fee):
        super().__init__(account_number, balance)
        self.transaction_fee = transaction_fee

    def withdraw(self, amount):
        calcu_tsf = (amount / 100) * self.transaction_fee
        amount -= calcu_tsf
        self.balance -= amount

# account = SavingAccount(1, 500, 10)
# account.display_balance()
# account.apply_interest()
# account.display_balance()

checking_account = CheckingAccount(2, 500, 10)
checking_account.display_balance()
checking_account.withdraw(50)
checking_account.display_balance()




