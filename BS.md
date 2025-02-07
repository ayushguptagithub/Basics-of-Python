class Ltc:
    acNo=2025000
    def __init__(self, name , phone , age,amount):
       self.name = name
       self.phone  = phone
       self.age = age 
       self.amount = amount 
       Ltc.acNo += 1
       self.acNo = Ltc.acNo
       self.password = 0
       self.passFlag = False
       print("Account created,Your Account NUmber is :",self.acNo)
       self.freeze = False
    
    def deposit(self,amount):
        self.amount+=amount
        print("amount available:", self.amount)
    
    def withdraw(self, amount):
        if (self.amount-amount) <3000:
            print("It reaches Minimum Level")
        else:
            self.amount-=amount
            print("amount available :", self.amount)
        
    def display_balance(self):
        print(f"your account balance is {self.amount}")
    def change_password(self, password):
        self.password = password
        print("Successfully changed Password")
customers = {}
while True:
    ch = int(input("press 1:To create an account\nPress 2 :TO use ATM\nPress 3 : To exit\nChoice:"))
    
    if ch == 1:
        name=input("Enter your name : ")
        phn=int(input("Enter your phone number : "))
        print("Your  age should be more than 18 to be eligible to create an account.")
        while True:
            age=int(input("Enter your Age : "))
            if age<18:
                print("You are not eligible to create account.")
            else:
                break
            
        while True:
            amt=float(input("Enter the amount : "))
            if amt<3000:
                print("To create an account minimum balance is 3000.")
            else:
                break
        
        obj = Ltc(name,phn,age,amt)
        customers.update({obj.acNo:obj})
    
    
    elif ch == 2:
        count = 0
        login = False
        while login==False:
            actNo=int(input("Enter your account number:"))
            if actNo in customers:
                obj = customers[actNo]
                if obj.passFlag == False:
                    password = int(input("Set your Password : "))
                    obj.password = password
                    obj.passFlag = True
                else:
                    count = 0
                    while count <3:
                        password = int(input("Enter your Password : "))
                        if obj.password == password:
                            print(obj.name,"Welcome to LTC Bank")
                            login = True
                            break
                        else:
                            count+=1
                    else:
                        obj.freeze = True
                        print("Account got freezed")
                    
            else:
                print("Wrong Account number.")
        
        while obj and obj.freeze!=True:
            ch = int(input("press 1:To Deposit\nPress 2 :TO Withdraw\nPress 3 : To Check Balance\nPress 4: to change password\nPress 5:Exit\nChoice:"))
            if ch == 1:
                amt=float(input("Enter the amount : "))
                obj.deposit(amt)
            elif ch == 2:
                amt=float(input("Enter the amount : "))
                obj.withdraw(amt)
            elif ch == 3:
                obj.display_balance()
            elif ch == 4:
                old_password =int(input("Enter the old password:"))
                if old_password == obj.password:
                    new_password = int(input("Enter the new password:"))
                    obj.change_password(new_password)
                else:
                    print("Wrong old password")
            elif ch == 5:
                print("Exiting......")
                break
            else:
                print("Invalid Option")
                
    elif ch==3:
        print("Exiting......")
        break
    else:
        print("Invalid Option")
else:
    print("Your Account has been Freezed")
        
        
        
        

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    