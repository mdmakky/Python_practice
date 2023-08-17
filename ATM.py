class ATM:
    def __init__(self) -> None:
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = int(input("""How can I help you?
              1. Creat account.
              2. Check balance.
              3. Change pin.
              4. Withdraw.
              5. Anything else to exit.
              """))
        if user_input == 1:
            self.creat_acc()
        elif user_input == 2:
            self.check_balance()
        elif user_input == 3:
           self.change_pin()                        
        elif user_input == 4:
            self.withraw()            
        else: 
            print("Thank you for being with us.")
            
#creat account mathod......
    def creat_acc(self):
            user_pin = int(input("Enter your pin: "))
            self.pin = user_pin
            user_balance = int(input("Enter your balance: "))
            self.balance = user_balance
            self.menu()

#check balance method.........           
    def check_balance(self):
            user_current_pin=int(input("Enter your pin: "))
            if user_current_pin==self.pin:
                print("Your current balance is",self.balance,"tk.")
                self.menu()
            else:
                print("Wrong pin!")
                self.menu()
        
#pin changing method......

    def change_pin(self):
        user_current_pin = int(input("Enter yout current pin."))
        if user_current_pin == self.pin:
            i = 3
            while i >= 1:
                    user_new_pin1 = int(input("Enter new pin:"))
                    user_new_pin2 = int(input("Enter new pin again: "))
                    if user_new_pin1 == user_new_pin2:
                        self.pin = user_new_pin2
                        print("Your pin changed succesfully!")
                        self.menu()
                    else:
                        print("Pin did not match.")
                        i = i-1
                        self.menu()
#withraw method..........                 
    def withraw(self):
        amount=int(input("Enter amount."))
        if self.balance>=amount:
            self.balance=self.balance-amount
            print("Witdraw successfull. Curent balance",self.balance,"tk.")
            self.menu()
        else:
            print("You dont have sufficient balance.")
            self.menu()
        
        

user1 = ATM()
