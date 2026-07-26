# Abstraction- 
# Abstraction means hiding unnecessary implementation details and showing only the essential functionality to the user.
# An ATM is a good example of abstraction. As a user, I can withdraw money, deposit money, or check my balance without knowing how authentication, database communication, transaction processing, and balance updates happen internally. Only the necessary functionality is exposed."
# need-"Abstraction reduces complexity, hides unnecessary implementation details, provides a common contract for child classes, and makes code easier to maintain and extend."

from abc import ABC,abstractmethod

class Payment(ABC):

    @abstractmethod 
    def pay(self,amount):
        pass

class UPIPayment(Payment):

    def pay(self, amount):
        print(f"paid ${amount} using UPI")
    
class CreditCardPayment(Payment):
    
    def pay(self,amount):
        print(f"paid ${amount} using Credit card")

obj = UPIPayment()
obj.pay(2000)

obj2 =CreditCardPayment()
obj2.pay(1000)

#2nd example-

from abc import ABC, abstractmethod

class Employee(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):

    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


class ContractEmployee(Employee):

    def __init__(self, name, hours, rate):
        super().__init__(name)
        self.hours = hours
        self.rate = rate

    def calculate_salary(self):
        return self.hours * self.rate


e1 = FullTimeEmployee("Vishal", 50000)
e2 = ContractEmployee("Rahul", 100, 400)

print("full time emp salary:",e1.calculate_salary())
print("Contract based emp salary:",e2.calculate_salary())