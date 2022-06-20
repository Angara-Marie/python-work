from datetime import datetime
class Account:
    def __init__(self, account_name, account_number):
        self.account_name = account_name
        self.account_number = account_number
        self.balance = 0
        self.deposits = []
        self.withdrawals= []
        self.transaction = 100
        self.loan = 0
        self.statement = [] 
    def deposit(self,amount):
        if amount<=0:
            return f"Deposit amount must be greater than 0"
        else:
            self.balance += amount
            now = datetime.now()
            transaction={
                "amount":amount,
                "time":now,
                "Narration":"Deposit made"
           }
            self.deposits.append(amount)
            self.statement.append(transaction)
            print(self.deposits)
            return f"Hello {self.account_name} you made a deposit of {amount} your balance is {self.balance} and your deposits are {self.deposits}."


    def withdraw(self, withdrawal):
        if withdrawal > self.balance - self.transaction:
            return f"Insufficient funds"
        elif withdrawal <= 0:
            return f"Amount must be greater than 0"
        else:
            self.balance -= withdrawal + self.transaction
            now = datetime.now()
            transaction = {
                "amount":withdrawal,
                "time":now,
                "Narration":"You have withdrawn"
            }
            self.withdrawals.append(withdrawal)
            self.statement.append(transaction)
            return f"Hello {self.account_name}, you made a withdrawal of {withdrawal} your new balance is {self.balance} and the withdrawals are{self.withdrawals}."  

    def deposit_statements(self):
         for a in self.deposits:
             print(a, end="\n")      

    def withdrawals_statement(self):
        for b in self.withdrawals:
            print(b,end="\n")

    def current_balance(self):
        return f"{self.balance}"  


    def full_statement(self):
        for transaction in self.statement:
             amount = transaction["amount"]
             Narration= transaction["Narration"]
             date= datetime.now().strftime("%x %X")
             print(f"{date}:   {Narration}   {amount}")  
             
    def borrow(self,amount):    
        number_of_deposits = len(self.deposits)
        loan_limit = sum(self.deposits)*1/3
        amount+=(amount)*0.03
       
        if amount<=100:
            return f"Your loan must be more than 100 "
        elif self.loan>0:
            return f"Dear customer you have an outstanding loan of {self.loan}"
        elif number_of_deposits<10:
            return f"Dear customer, you must have atleast 10 deposits"

        elif amount>=loan_limit:
            return f"Dear customer you can't borrow {amount}is higher than a limit of {self.balance}"

        else:
            self.loan+=amount
            return f"Dear customer {self.account_name} your loan of ksh{amount} has been granted successfully"  


    def loan_repay(self,amount):
        if amount<self.loan:
            payment = self.loan-amount
            return f"Dear customer you have paid {amount} and your loan balance is {payment}"
        else:
            over_pay = amount-self.loan
            self.balance+=over_pay
            return f"Loan successfuly paid,the over pay is {over_pay} and your new balance is {self.balance}" 


    def transfer(self,amount,account):
        fee= amount*0.05
        total_amount=fee+amount
        if amount<=0:
            return f"Dear customer {self.account_name} your balance is insufficient"
        elif total_amount>self.balance:
            return f"Dear customer {self.account_name} you balance is {self.balance} and you need atleast {total_amount}"
        else:
            self.balance-=total_amount
            return f"Dear customer you  have sent {amount} to {account} and your new balance is {self.balance}"               


   
