#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 21:56:01 2018

@author: Sanket
"""
import random
import sys
print("*"*22+"Welcome to Swiggy"+"*"*22)
print()
print('{:^60}'.format("Have a Break, Have a Swiggy"))
print()
class Swiggy():
    minimum_balance=0
    def __init__(self):
        self.balance = 0
        self.bill = 0
#        self.amount=0
    
        
        
    def get_user_details(self,city='Mumbai'):
        self.account_id=random.randint(100,500)
        self.account_name=input("Enter name:")
        self.account_address=input("Enter Address:")
        self.order_id=random.randint(100,500)
        self.city=city
        
        
                
    def hotels(self):
        self.hotel_id=random.randint(500,1000)
        print("1.Wadeshhwar")
        print("2.Sai Leela")
        print("3.Ambika")
        ch=int(input("Enter choice"))
        if(ch==1):
            self.hotel_name='Wadeshwar'
        elif(ch==2):
            self.hotel_name='Sai Leela'
        elif(ch==3):
            self.hotel_name='Ambika'
            
    
    def get_acc_balance(self):
        return self.balance
    

    def get_order_items(self):
        choice={'Pizza':100 , 'Burger':150,'Pav Bhaji':150,'Maggi':100,'Noodles':150}
        print("1.Pizza")
        print("2.Burger")
        print("3.Pav Bhaji")
        print("4.Maggi")
        print("5.Noodles")
        while(True):
            food=input("Enter food:")
            for key,value in choice.items():
                if food==key:
                    self.bill+=value
            ch=input("Do you want to add more food:")
            if ch=='y':
                break
        print("Your Bill is :{} ".format(self.bill) )    
        return self.bill

    def get_order_details_payment(self,balance):
        self.order_id=random.randint(100,500)
        a=Swiggy().get_order_items()
        
#        print(self.get_acc_balance())
#        print(balance)
        
        
        if balance>a:
            balance-=a
            print("Order Placed Sucessfully")
            print("Remaining Balance:{}".format(balance))
        else:
            print("Insufficient Fund")
        
                
    def deposit_amount(self,amount):
        self.balance+=amount
        return self.balance
        
    def display(self):
        print('Account_No  Name  City  Address  Balance  ')
        print( self.account_id,self.account_name,self.account_address,self.city ,self.get_acc_balance())
#        print('Hotel Id  Hotel Name ')
        
def Display(swigs):#,hotel):
    for account in swigs.values():
        account.display()
#    for account1 in hotel.values():
#        account.displaaccount.get_acc_balance()y()
        
        
        
        
def main():
    swigs = {} 
#    hotel={}
    order={}
    while True:
        print('{:^60}'.format("Home"))
        print()
        print("1.Create a New Account")
        print("2.View Account Details and Hotel Details ")
        print("3.Place an order")
        print("4.Check Balance")
        print("5.Add Money To Swiggy Balance")
        print("6.Exit")
        ch=int(input("Enter choice:"))
        if ch==1:
            account=Swiggy()
            account.get_user_details()
            swigs[account.account_id]=account#.account_name,account.account_address,account.city,account.get_acc_balance())
#            print(swigs)
        
        if ch==2:
            Display(swigs)
#            Display(hotel)
            
        if ch==3:
#            print("Select Hotel:")
            account1=Swiggy()
            account1.hotels()
            r=account.get_acc_balance()
            account1.get_order_details_payment(r)
            order[account.order_id]=account
            
        if ch==4:
            r=account.get_acc_balance()
            print(r)
            
        if ch==5:
            acc =int(input('Deposit account: '))
            amount = int(input('Enter amount to deposit: '))
            swigs[acc].deposit_amount(amount)
#            balance+=amount
#            account.balance+=amount
            
        else:
            sys.exit()
            
            
            
            
            
            
                        
            
if __name__ == '__main__':
    main()           

                
        
        
    

        
        
        
        
        
        
        