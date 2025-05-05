class Account:

    def __init__(self, name):
        self.name = name
        self.transactions = []
        self.balance = 0.0


    def deposit(self, amount):
        if amount <= 0: raise ValueError("Deposit amount cannot be negative")
        self.balance += amount
        self.transactions.append({"Deposited": amount})

    def withdraw(self, amount):
        if amount <= 0: raise ValueError("Withdraw amount cannot be negative")
        if amount > self.balance: raise ValueError("Withdraw amount cannot be greater than balance")
        self.balance -= amount
        self.transactions.append({"Withdrawn": amount})

    def get_balance(self):
        return self.balance

    def view_history(self, ):
        counter = 0
        for transaction in self.transactions:
            print(transaction)
            counter += 1
        return counter

