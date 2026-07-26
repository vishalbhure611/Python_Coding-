# Encapsulation:
# Encapsulation means wrapping data (variables) and the methods that operate on that data into a single unit, usually a class, and controlling direct access to that data.
# In simple words:Keep data and the methods that work on it together, and restrict direct modification of sensitive data.
# eg- BankAccount would be great example for encapsulation.in which user should not be able to directly change  their account balancce instead the balance should be modified using controlled methods such as withdraw and deposit.
# python uses acces modifiers such as public ,private, and protect to implement encapsulation which  ensures security.

class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance            #private var
    
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print(f"{amount} amount deposited, current balance: {self.__balance}")
        else:
            print("enter valid amount")
    
    def withdraw(self,amount):
        if amount <=self.__balance:
            self.__balance -=amount
            print(f"{amount} amount withdrawn, current balance: {self.__balance}")
        else:
            print("Insufficient balance")
    
    def get_balance(self):
        return 'current balance:' ,self.__balance
    
account = BankAccount("Vishal",1000)
print(account.get_balance())
account.deposit(100)
account.withdraw(100)