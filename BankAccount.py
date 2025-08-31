class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Недостаточно средств")

    def get_balance(self):
        return self.__balance


account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
print("Текущий баланс:", account.get_balance())  
account.withdraw(2000)  
