**Bank System**
```Python  
class Bank:
    account_number_generator=20250
    def __init__(self,name,gender,amount):
        self.name=name
        self.gender=gender
        self.amount=amount
        Bank.account_number_generator+=1
        self.account_no=Bank.account_number_generator
        self.password = 0
        self.status = False
        self.login = False
        print("Congrats",self.name,"Account created and your Account number is:",self.account_no)
    def withdraw(self,amount):
        if self.amount-amount>=3000:#allowed
            self.amount=self.amount-amount
            print("Account number:",self.account_no,"balance left:",self.amount)
        else:
            print("Account number:",self.account_no,"not enough balance left")

    def deposit(self,amount):
        if amount>0:#allowed
            self.amount=self.amount+amount
            print("Account number:",self.account_no,"balance left:",self.amount)
        else:
            print("Amount can not be -ve")
    def check_balance(self):
        print("Account number:",self.account_no,"On Name of:",self.name,"Balance:",self.amount)
    def resetPassword(self):
        while True:
            oldpassword = int(input("Enter your old password:"))
            if oldpassword != self.password:
                print("Wrong password")
            else:
                self.password = int(input(" Enter New Password:"))
                print("Password reset Successfully")
                break

#creat menu driven code for bank management
'''
1.open new account: takes name,gender,3000+amount then create account
2.withdraw: takes account number,if there then reads amount and removes it from
account number.
3.deposite: takes account number,if there then reads amount and adds it to
account number.
4.check balance:takes account number,if there then prints de
account number.
'''
d = {}

while True:
    ch = int(input("Press 1:to create an account\nPress 2 :Atm System\n3:Exit\nEnter Your choice:"))
    if ch==1:
        #main design
        name=input("Enter name:")
        gender=input("Enter gender:")
        print("To open account we need minimum 3000")
        while True:
            amount=float(input("Enter Amount:"))
            if amount>=3000:
                b=Bank(name,gender,amount)
                d.update({b.account_no:b})
                break
            else:
                print("To open account we need minimum 3000")
    elif ch==2:
        
        while True:
            acc_no=int(input("Enter Account Number"))
            if acc_no in d.keys():
                obj = d[acc_no] 
                break
            else:
                print("Wrong Account Number:")
        while obj:
            if obj.status == False:
                password = int(input("Set pin:"))
                obj.password = password
                obj.status= True
                obj.login = True
            else:
                if obj.login==False:
                    password = int(input("Enter your password:"))
                if password == obj.password:
                    obj.login = True
                    work = int(input("Press 1 :deposit\nPress 2:Widthdrawal\n3:Check Balance\n4.Reset Password\n5:Exit"))
                    if work==1:
                        
                        amount = float(input("Enter The amount"))
                        if amount >0:
                            obj.deposit(amount)
                        else:
                            print("You cannot deposit negative amount")
    
                    elif work == 2:
                        
                        amount = float(input("Enter The withdrawal"))
                        if amount > 0:
                            obj.withdraw(amount)
                        else:
                            print("You cannot Withdraw negative amount")
                    elif work == 3:
                        obj.check_balance()
                    elif work == 4:
                        obj.resetPassword()
                    elif work==5:
                        print("Exiting....")
                        obj.login = False
                        break
                    else:
                        print("Invalid option")
                else:
                    print("Wrong password")
                


    elif ch==3:
        print("Exiting....")
        break
    else:
        print("Invalid Option")
        
```