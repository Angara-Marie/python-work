class Account:
    def __init__(self, account_name, account_number):
        self.account_name = account_name
        self.account_number = account_number
        self.balance = 0
        self.deposits = []
        self.withdrawals= []
    def deposit(self,amount):
        if amount<=0:
            return f"Deposit amount must be greater than 0"
        else:
            self.balance += amount
            self.deposits.append(amount)
            print(self.deposits)
            return f"Hello {self.account_name} you made a deposit of {amount} your balance is {self.balance} and your deposits are {self.deposits}."


    def withdraw(self, withdrawal):
        self.transaction = 100
        if withdrawal > self.balance:
            return f"Insufficient funds"
        elif withdrawal <= 0:
            return f"Amount must be greater than 0"
        else:
            self.balance -= withdrawal + self.transaction
            self.withdrawals.append(withdrawal)
            return f"Hello {self.account_name}, you made a withdrawal of {withdrawal} your new balance is {self.balance} and the withdrawals are{self.withdrawals}."  

    def deposit_statements(self):
         for a in self.deposits:
             print(a, end="\n")      

    def withdrawals_statement(self):
        for b in self.withdrawals:
            print(b,end="\n")

    def current_balance(self):
        return f"{self.balance}"                  

