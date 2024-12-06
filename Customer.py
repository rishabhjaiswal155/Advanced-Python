#Bank Application
import sys
class Customer:
    '''Customer class of Bank Application'''
    bankname='Rishabh Bank'
    def __init__(self,name,city,balance=0.0):
        self.name=name
        self.city=city
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
        print("Balance after deposit:",self.balance)
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
            print("Balance after withdraw:",self.balance)
        else:
            print("Insufficient funds to withdraw!!")
    def displayinfo(self):
        print("Customer name:",self.name)
        print("Customer city:",self.city)
        print("Customer Balance:",self.balance)
        print()
print("Welcome to",Customer.bankname)
c=Customer('Rishabh','Akola')
while True:
    print("options are:\nd-deposit\nw-withdraw\nc-displayinfo\ne-exit\n")
    print("Choose the option:")
    option=input("Enter the option:").lower()
    if option=='d':
        amount=float(input("Enter amount to deposit:"))
        c.deposit(amount)
    elif option=='w':
        while True:
            amount=float(input("Enter amount in multiples of 100 to withdraw:"))
            if not(amount>0 and amount%100==0):
                print("Invalid amount!!")
                break
            else:
                c.withdraw(amount)
                break
    elif option=='c':
        print("Customer Details are:")
        c.displayinfo()
    elif option=='e':
        print("Thank You for Banking with",Customer.bankname)
        sys.exit(0)
    else:
        print("Invalid Option!!!")
        
