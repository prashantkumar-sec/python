# Classes & Objects (OOP basics):

class Account:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance!")
        else:
            self.balance -= amount

Acc = Account("Prashant",1000)
Acc.deposit(500)
Acc.withdraw(2000)      # Insufficient Balance!