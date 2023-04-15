class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    def make_deposit(self, amount):
        self.account.deposit(100)
        return self

    def make_withdraw(self, amount):
        self.account.withdraw(50)
        return self

    def display_user_balance(self):
        print(f"current balance is {self.account}")
        self.account.display_account_info()
        return self 
        




class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        # your code here! (remember, instance attributes go here)
        self.int_rate = int_rate
        self.balance = balance 
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount #self.balance = self.balance + amount
        print(f"{amount} has been deposited into your account")
        
    def withdraw(self, amount):
        self.balance -= amount #self.balance = self.balannce -amount
        if amount > self.balance:
            print("insufficient funds")
            self.balance -= 5
        else: 
            print(f"{amount} has been withdrawn from your account")
            
            
        
        # your code here
    def display_account_info(self):
        # your code here
        print(f"Your current balance is {self.balance}")
        
    def yield_interest(self):
        interest = self.int_rate * self.balance
        self.balance += interest 
        print(f"your current balance with interest is {self.balance}")
    

user1 = User("me", "me@gmail.com")
user1.make_deposit(100).make_withdraw(50).display_user_balance()




