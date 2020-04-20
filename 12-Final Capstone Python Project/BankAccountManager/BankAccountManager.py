# -*- coding: utf-8 -*-
# script bonjour.py
from tkinter import *

'''
anna = Customer('Anna', 1234)
anna.open_checking(1111, 1000)
anna.open_checking(2222, 3000)
anna.get_total_deposits()

make_deposit(anna, 'C', 2222, 12)
anna.get_total_deposits()

make_withdraw(anna, 'B', 4444, 80000)
anna.get_total_deposits()
'''

from customers import Customer

def make_deposit(client, acct_type, acct_nbr, deposit_amnt):
    """
    make_deposit(name, acct_type, acct_nbr, deposit_amnt)
    client       = variable name (Customer record) 
    acct_type    = string 'C' checking, 'S' savings, 'B' business
    acct_nbr     = integer
    deposit_amnt = integer
    """
    for acct in client.accts[acct_type]:
        if acct.acct_nbr == acct_nbr:
            acct.deposit(deposit_amnt)
            

def make_withdraw(client, acct_type, acct_nbr, withdraw_amnt):
    """
    make_deposit(name, acct_type, acct_nbr, deposit_amnt)
    client       = variable name (Customer record) 
    acct_type    = string 'C' checking, 'S' savings, 'B' business
    acct_nbr     = integer
    withdraw_amnt = integer
    """
    for acct in client.accts[acct_type]:
        if acct.acct_nbr == acct_nbr:
            acct.withdraw(withdraw_amnt)
            

def create_customer():
    global client
    client = Customer( name.get(), int(pin.get()) )
    Label(root, text=f'Client {name.get()} is saved.').grid(row=3, column=1)
    #root.destroy()

def open_account():
    client.open_checking(   int(acct_nbr.get()), int(init_dep.get())   )
    Label(atm_win, text=f'Account {int(acct_nbr.get())} is saved.').grid(row=3, column=1)

def check_balance():
    result = client.get_total_deposits()
    Label(atm_win, text=result).grid(row=8, column=1)
    Label(atm_win, text='').grid(row=9, column=1)

def new_window():
    global atm_win
    try:
        if atm_win.state() == "normal": atm_win.focus()
    except NameError as e:
        #print(e)
        atm_win = Toplevel()
        #atm_win.geometry("300x300+500+200")
        Label(atm_win, text='Open checking account').grid(row=0)
        
        Label(atm_win, text='Account number: ').grid(row=1)
        Label(atm_win, text='Initial deposit: ').grid(row=2)
        Label(atm_win, text='').grid(row=3, column=1)

        global acct_nbr
        global init_dep
        acct_nbr = Entry(atm_win)
        init_dep = Entry(atm_win)
        acct_nbr.grid(row=1, column=1)
        init_dep.grid(row=2, column=1)

        Button(atm_win, text='Create',
            command=open_account).grid(row=5, column=0, sticky=W, pady=4)

        Button(atm_win, text='Check balance',
            command=check_balance ) \
                    .grid(row=5, column=1, sticky=W, pady=4)
        Button(atm_win, text='Quit', command=root.quit).grid(row=6, column=0, sticky=W, pady=4)


if __name__ == "__main__":

    root = Tk()
    Label(root, text='Name: ').grid(row=0)
    Label(root, text='PIN: ').grid(row=1)
    Label(root, text='').grid(row=3, column=1)

    name = Entry(root)
    pin = Entry(root)

    name.grid(row=0, column=1)
    pin.grid(row=1, column=1)

    Button(root, text='Quit', command=root.quit).grid(row=4, column=0, sticky=W, pady=4)
    Button(root, text='Register', command=create_customer).grid(row=4, column=1, sticky=W, pady=4)

    Button(root, text="Open new Window", command=new_window).grid(row=5, column=1, sticky=W, pady=4)
    mainloop()

    








