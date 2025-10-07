#my code
class bankaccount:
    def __init__(self,acc_number,name,balance):
        self.acc_number=acc_number
        self.name=name
        self.balance=balance

    def deposit(self):
        print(f"----welcome---- {self.name}\n")

        try:
            deposit_amount=float(input("enter deposit amount\n"))
        except ValueError:
            print("enter numbers only\n")
            return
        
        if deposit_amount<0:
            print("enter positive amount\n")
            return

        if deposit_amount>=0:
            self.balance+=deposit_amount
            print("cash deposited successfully\n")

    def withdraw(self):
        try:
            withdraw_amount=float(input("enter withdraw amount\n"))
        except ValueError:
            print("enter numbers only\n")
            return
        
        if  withdraw_amount<0:
            print("enter positive amount\n")
            return
        
        if withdraw_amount>self.balance:
            print("insuffisient balance\n")
            return

        if withdraw_amount>=0:
            self.balance-=withdraw_amount
            print("cash withdrawed succesfully\n")

        

    def balan(self):
        print(f"your balance is:={self.balance}\n")

    
class savingsaccount(bankaccount):
    def __init__(self,acc_number, name, balance,interest_rate=10):
        super().__init__(acc_number,name, balance)
        self.interest_rate=interest_rate 

    def add_interest(self):
        interest=self.balance*(10/100)
        self.balance+=interest
        print(f"interest added for {self.name}.new balance={self.balance}\n")


accounts={}
next_acc_no=1000    

def create_account():
    global next_acc_no
    user_name=input("enter your name\n")
    account=savingsaccount(next_acc_no,user_name,0)
    accounts[next_acc_no]=account
    print(f"account created successfully! account number={next_acc_no}\n")
    next_acc_no+=1
                   

def access_account():
    try:
        acc_no=int(input("enter acc number\n"))
    except ValueError:
        print("enter numbers only\n")
        return  

    if acc_no not in accounts:
        print("account not found\n")
        return
    
    account=accounts[acc_no]
        
    while True:
        print("\n---menu---\n")
        print("press 1 to deposit")
        print("press 2 to withdraw")
        print("press 3 for check balance")
        print("press 4 for add interest")
        print("press 5 for exit")

        try:
            choice=int(input("enter choice to perrform\n"))
        except ValueError:
            print("enter numbers only\n")
            return
        
        if choice==1:
            account.deposit()
            
        elif choice==2:
            account.withdraw()

        elif choice==3:
            account.balan()

        elif choice==4:
            account.add_interest()

        elif choice==5:
            print("thank you")
            break



def main():
    print("welcome to simple bank system\n")
    while True:
        
        print("press 1 for create account")
        print("press 2 for access account")
        print("press 0 for exit")

        try:
            main_input=int(input("enter your choice\n"))
        except ValueError:
            print("enter numbers only\n")
            return
        
        if main_input==1:
            create_account()

        elif main_input==2:
            access_account()

        elif main_input==0:
            print("thank you\n")
            break

        else:
            print("invalid input\n")
        
main()        

        
           

        