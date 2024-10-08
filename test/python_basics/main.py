class BankAccount: 
    def __init__(self, acc_holder, balance=0):
        self.acc_holder = acc_holder
        self.balance = balance

    def deposit(self,amount): 
        self.balance += amount

    def withdraw(self,amount):
        self.balance -= amount

    def get_balance(self):
        return self.balance
    

if __name__ == "__main__":
    john_account = BankAccount("John Doe", 500)

    john_account.deposit(100)
    balance = john_account.get_balance()
    print("Balance is: ", balance)


