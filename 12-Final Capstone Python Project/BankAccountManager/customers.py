# -*- coding: utf-8 -*-
# script customers.py

from accounts import CheckingAccount, SavingsAccount, BusinessAccount

class Customer:
    
    def __init__(self, name, PIN):
        self.name = name
        self.PIN = PIN
        self.accts = {'C':[], 'S':[], 'B':[]}
        
    def __str__(self):
        return self.name
    
    def open_checking(self, acct_nbr, opening_deposit):
        self.accts['C'].append(CheckingAccount(acct_nbr, opening_deposit))
        
    def open_savings(self, acct_nbr, opening_deposit):
        self.accts['S'].append(SavingsAccount(acct_nbr, opening_deposit))
        
    def open_business(self, acct_nbr, opening_deposit):
        self.accts['B'].append(BusinessAccount(acct_nbr, opening_deposit))
        
    def get_total_deposits(self):
        total = 0
        for acct_type in self.accts.keys():
            for acct in self.accts[acct_type]:
                #print(f"{acct} \n")
                total += acct.balance
        return f"Combined Deposits: ${total:.2f}"