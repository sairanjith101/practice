class BankAccount:

    def __init__(self, account_number, initial_balance = 0):
        self.__account_number = account_number
        self.__balance = initial_balance

    def Deposite(self, amount):
        if self.__balance > amount:
            self.__balance += amount
            print(f'Deposite Rs.{amount}. New Balance Rs.{self.__balance}')
        else:
            print(f'Deposite amount must be positive')
    
    def Withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print(f'Withdraw Rs.{amount}. New Balance Rs.{self.__balance}')

    def get_account_number(self):
        return self.__account_number
    
    def get_current_balance(self):
        return self.__balance
    
bank = BankAccount("12345", 1000)

bank.Deposite(500)
bank.Withdraw(300)
print(bank.get_account_number())
print(bank.get_current_balance())