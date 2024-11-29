class bankaccount:
    def __init__(self,account_number,initial_balance = 0):
        self.__account_number = account_number
        self.__balance = initial_balance

    def deposite(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f'Deposte: Rs.{amount}. New Balance: Rs.{self.__balance}')
        else:
            print('Deposite amount must be positive')

    def withdraw(self, amount):
        if amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
                print(f'Withdraw: Rs{amount}. New Balance: Rs{self.__balance}')
        else:
            print("Withdraw amount must be positive")

    def get_account(self):
        return self.__account_number
    
    def get_balance(self):
        return self.__balance
    
account = bankaccount('12345', 1000)

print(f'Current Balance: Rs.{account.get_balance()}')

account.deposite(500)

account.withdraw(300)