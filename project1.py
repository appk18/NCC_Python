import random
class Bank:
    def __init__(self):
        print('\t\tWelcome from NCC Bank!')
        self.accounts = {} 
        self.current_accountno = None
        self.name = None
        self.password = None
        self.initial_deposit = None
    
    def main_menu(self):
        print('Press 1 to register\nPress 2 to log in\nPress 3 to log out')
        while 1:
            try:
                ch = int(input("Plese choose (1/2/3) : "))
                if ch == 1:
                    print("This is register page!")
                    self.register()
                elif ch == 2:
                    print("This is Log in page!")
                    self.login()
                elif ch == 3:
                    print("Bye! See you next time!")
                else:
                    print("Wrong Option!")
            except ValueError:
                print("Wrong Input ! You must enter 1/2/3.")
            else:
                return ch

    def beautify_print(self,message):
        print("******************")
        print(message)
        print("******************")

    def register(self):
        user_name = input("Plese enter you name : ")
        user_password = input("Plese enter your password : ")
        reenter_pass = input("Please enter your password again : ")
        if(user_password != reenter_pass):
            print("\t\tPassword are not the same!")
            self.register()
        else:
            deposit_amount = int(input("Please enter your depoist amount : "))
            self.create_account(user_name,user_password,deposit_amount)
            # print(f"Your current account number: {self.current_accountno}")
    
    def create_account(self, name, password, deposit):
        account_no = random.randint(100,999)
        self.accounts[account_no] = [name,password,deposit]
        self.name = self.accounts[account_no][0]
        self.password = self.accounts[account_no][1]
        self.initial_deposit = self.accounts[account_no][2]
        self.current_accountno = account_no
        self.beautify_print(f'Account created successfully!Your account number is {account_no}')
        print('Your Info\n******************')
        print('Your Name : ', self.name)
        print('Your Account Number : ', self.current_accountno)
        print('Your Amount : ', self.initial_deposit)
        self.main_menu()

    def checkdata(self, password, current_accountno):
        if password == self.accounts[current_accountno][1] and current_accountno in self.accounts.keys() : 
            return 1
        
    def login(self):
        login_acc = int(input("Enter Account Number : "))
        login_pass = input("Enter your password : ")
        if self.checkdata(login_pass, login_acc) == 1:
            self.beautify_print("Log in successful!")
            self.activity()
        else:
            print("Account and Password are not correct!")
            self.main_menu()

    
    def activity(self):
        while 1:
            try:
                act = int(input("Press 1 to withdraw\nPress 2 to deposit\nPress 3 to transfer\nPress 4 to exit\nPlease choose your options : "))
                if act == 1:
                    withdraw_amount = int(input("How much you want to widthdraw : "))
                    if withdraw_amount <= self.initial_deposit:
                        balance = self.initial_deposit - withdraw_amount
                        print("Your Balance (after withdraw) is ", balance)
                    else: 
                        print("You don't have enough money! ")
                elif act == 2:
                    deposit_amount = int(input("How much you want to deposit : "))
                    new_amount = self.initial_deposit + deposit_amount
                    print("Your Balance (after deposit) is ", new_amount)
                elif act == 3:
                    print("Still in Progress")
                elif act == 4: 
                    print("Thank you for using NCC Bank! See you again!")
                else:
                    print("Wrong option! Please enter 1/2/3/4")
            except ValueError:
                print("Wrong Input ! You must enter 1/2/3/4.")
            else: 
                return act
                        
if __name__ == '__main__':
    bank = Bank()
    bank.main_menu()

    