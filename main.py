
class BankAccount:
    def __init__(self,name,pin):
        self.name=name
        self.pin=pin
        self.balance=0.0

    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f'{amount}₹ Credited sucessfully')
        else:
            print("enter positve number")
    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient Balance")
        elif amount <=self.balance:
            self.balance-=amount
            print(f'{amount}₹ Debited to your account')
            print("Do You want see Your available balance:\n1:Yes\n2:No")
            choose=int(input("Choose:"))
            if choose==1:
                print(f"Your Available balance Is:{self.balance}₹")
            elif choose==2:
                print("thank you")
    def checkbalance(self):
        print(f'Current balance💳:{self.balance}₹')
    def Exit(self):
        print("Thank you visit Again🙏🏾")
        
        
name=input("Enter Your name:")
pin=int(input("Enter Your Pin:"))
B=BankAccount(name,pin)
while True:
    print("1: Deposite\n2: Withdraw\n3: Check Balance\n4: Exit")
    choice=input("Choose Bank Status:")
    if choice=="1":
        amount=float(input("Enter amount to Deposit💶:"))
        B.deposit(amount)
    elif choice=="2":
        amount=float(input('Enter amount to withdraw💸:'))
        B.withdraw(amount)
    elif choice=="3":
        B.checkbalance()
    elif choice=="4":
        B.Exit()
        break
    else:
        print("invalid Input")

        