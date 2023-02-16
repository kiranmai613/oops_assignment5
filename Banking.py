class Account:  #create class 
    def __init__(self,title=0,Balance=0):
        self.title=title
        self.Balance=Balance


class SavingsAccount(Account):  #create subclass
    def __init__(self,title,Balance,interestRate):
        self.interestRate=interestRate
        super().__init__(title,Balance)
        
        

    def display(self): 
     return(f"{self.title} is the title , and the {self.Balance} is the account balance and {self.interestRate} is the interrestRate")

obj=SavingsAccount("sia",5000,2)
print(obj.display())