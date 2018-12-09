import random

import sys


class Banking():
    min_balance = 0

    def __init__(self):
        self.balance = 0

    def create_account(self, acc_type='Savings'):
        self.account_no = random.randint(100, 300)
        self.name = input("Enter name:")
        self.acc_type = acc_type

    def getbalance(self):
        return self.balance

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print("Insufficient Balance")

    def deposit(self, amount):
        self.balance += amount

    def display(self):
        print("Account no    Name    Account Type    Balance")
        print(self.account_no, self.name, self.acc_type, self.balance)


def Display(accounts):
    for i in accounts.values():
        i.display()


def main():
    accounts = {}
    while True:

        print("1.Create Account")
        print("2.Get Balance")
        print("3.Withdraw")
        print("4.Deposit")
        print("5.Display Info")
        ch = int(input("Enter Choice:"))
        if ch == 1:
            account = Banking()
            account.create_account()
            accounts[account.account_no] = account
            print("Account Created Successfully")
        elif ch == 2:
            print(account.getbalance())
        elif ch == 3:
            acc=int(input("Withdraw Account:"))
            amount = int(input("Enter Amount to be withdrawn"))
            accounts[acc].withdraw(amount)
        elif ch == 4:
            acc = int(input("Withdraw Account:"))
            amount = int(input("Enter Amount to be Added"))
            accounts[acc].deposit(amount)
        elif ch == 5:
            Display(accounts)


main()
