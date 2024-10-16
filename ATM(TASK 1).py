class ATM:
    def __init__(self, balance=0):
        self.balance= balance
    default_pin= 1234 
    def auth(self):
        attempt=0
        while(attempt<3):
            print("Enter your 4 digit login pin")
            pin=int(input( ))
            if pin == self.default_pin:
                print("Authentification successful")
                return True
            else:
                attempt=attempt+1
                print("Incorrect pin,try again,You have maximum 3 attempts")
            return False
    def menu(self):
        print("Services available:")
        print("1. Check balance")
        print("2.Withdraw cash")
        print("3.Deposit")
        print("4.Exit")
    def check_bal(self):
        print("Your account balance is:", balance)
        
    def Withdraw(self, amount):
        if self.balance < amount :
            print("You can not withdraw")
        else:
            self.balance=self.balance-amount
            print("Your current balance is:",self.balance)
            
    def depo(self,amount):
        self.balance=self.balance+ amount
        print("Current balance is:",self.balance)
        
        
    def run(self):
        if self.auth():
            while True:
                self.menu()
                choice=int(input("Enter your choice"))
                if choice==1:
                    self.check_bal()
                    break
                elif choice==2:
                    amount=float(input("Enter the amount you want to withdraw"))
                    self.Withdraw(amount)
                    break
                elif choice==3:
                    amount=float(input("Enter the amount you want to deposit"))
                    self.depo(amount)
                    break
                elif choice==4:
                    print("Thank you, Please visit again")
                    break
                else:
                    print("Invalid input")
                    
if __name__== "__main__":
    atm= ATM()
    atm.run()
            
                
            
        
