class Account:
    def __init__(self, account_name, account_number, balance):
        self.account_name = account_name
        self.account_number = account_number
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        return f"Hello {self.account_name} you made a deposit of {amount} and your balance is {self.balance}."

    def withdraw(self, withdrawal):
        self.balance -= withdrawal
        return f"Hello {self.account_name}, you made a withdrawal of {withdrawal} your new balance is {self.balance}."    
