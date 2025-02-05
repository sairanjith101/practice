class BankAccount:
    
    def __init__(self, account_number, initial_balance = 0):
        self.__account_number = account_number
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f'Deposite amount ${amount}. New Balance ${self.__balance}' )
        else:
            print("Deposite amount must be Positive")

    def withdraw(self, amount):
        if amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
                print(f'Withdraw amount ${amount}. New Balance ${self.__balance}')
            else:
                print("Insufficend Balance")
        else:
            print("Deposite amount must be positive")

    def get_account_number(self):
        return self.__account_number
    
    def get_balance(self):
        return self.__balance

bank = BankAccount('12345', 1000)
bank.deposit(500)
bank.withdraw(300)
print(bank.get_account_number())
print(bank.get_balance())