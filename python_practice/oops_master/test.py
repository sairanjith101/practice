class BankAccount:
    def __init__(self, accont_number, initial_balance = 0):
        self.__account_number = accont_number
        self.__balace_amount = initial_balance
    
    def Deposit(self, amount):
        if amount > 0:
            self.__balace_amount += amount
            print(f'Deposit Rs.{amount}. New Balance Rs.{self.__balace_amount}')
        else:
            print("Deposit amount must be positive ")
    
    def Withdraw(self, amount):
        if amount > 0:
            if self.__balace_amount >= amount:
                self.__balace_amount -= amount
                print(f"Withdraw Rs.{amount}. Current Balance Rs.{self.__balace_amount}")
            else:
                print("Withdraw amount must be positive")
    
    def get_account_number(self):
        return self.__account_number
    
    def get_balance(self):
        return self.__balace_amount

account = BankAccount("1234", 1000)
account.Deposit(500)
account.Withdraw(300)
