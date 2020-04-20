# -*- coding: utf-8 -*-
# script accounts.py

# Abstract class
class Account:
    
    def __init__(self, acct_nbr, opening_deposit):
        self.acct_nbr= acct_nbr
        self.balance = opening_deposit
        
    def __str__(self):
        return f'Balance: {self.balance:.2f}'
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('Insufficiant Funds.')


class CheckingAccount(Account):
    
    def __init__(self, acct_nbr, opening_deposit):
        Account.__init__(self, acct_nbr, opening_deposit)
    
    def __str__(self):
        return f"Checking account: #{self.acct_nbr}\nBalance: ${self.balance:.2f}"

    
class SavingsAccount(Account):
    
    def __init__(self, acct_nbr, opening_deposit):
        super().__init__(acct_nbr, opening_deposit)
    
    def __str__(self):
        return f"Savings account: #{self.acct_nbr}\nBalance: ${self.balance:.2f}"
    
    
class BusinessAccount(Account):
    
    def __init__(self, acct_nbr, opening_deposit):
        super().__init__(acct_nbr, opening_deposit)
    
    def __str__(self):
        return f"Business account: #{self.acct_nbr}\nBalance: ${self.balance:.2f}"
    
    