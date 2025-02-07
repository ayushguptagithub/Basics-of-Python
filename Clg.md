class LTCE:
    roll = 20250000
    fee = 70000
    def __init__(self,name,phone,dob,branch,year):
        self.name = name
        self.phone = phone
        self.dob = dob
        self.branch = branch
        self.year = year
        LTCE.roll += 1
        
        self.roll = LTCE.roll
        self.fees = fees
        print("Your Admission is Sucessfull,your rollno is ",self.roll)
        
    def payfees(self,amount):
        if amount==(LTCE.fees/2):
            self.fees+=amount
            print("You paid the full fees")
        else:
            print("your total fees to be paid is ,",(LTCE.fees-self.fees))
        
    def checkfees(self):
        print("your balanced fees is",(LTCE.fees-self.fees))

ch = int(input("""
press1:To Get Admission
press2: To 
    """))
        
        