"""Employee pay calculator."""
"""First attempt"""

class Employee:
    def __init__(self, name):#, 
        self.name = name

    def get_pay(self):
        pass

    def __str__(self):
        return self.name

class SalaryMan(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary
    def get_pay(self):
        return self.salary
    def __str__(self):
        string = self.name + " works on a monthly salary of "+ str(self.salary) +". Their total pay is " + str(self.salary) + "."
        return string
                
class Wage(Employee):
    def __init__(self, name, wage, hours):
        super().__init__(name)
        self.wage = wage
        self.hours = hours
    def get_pay(self):
        payment = self.wage*self.hours
        return (payment)
    def __str__(self):
        string = self.name + " works on a contract of "+ str(self.hours) +" hours at " + str(self.wage) +"/hour. Their total pay is " + str(self.wage*self.hours) + "."
        return string

class BonusCommisionSalary(SalaryMan):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus
    def get_pay(self):
        payment = self.salary + self.bonus
        return (payment)  
    def __str__(self):
        string = str(self.name + " works on a monthly salary of "+ str(self.salary) +" and receives a bonus commission of "+ str(self.bonus) +". Their total pay is " + str(self.salary + self.bonus) + ".")
        return string
    
class BonusCommisionWage(Wage):
    def __init__(self, name, wage, hours, bonus):
        super().__init__(name, wage, hours)
        self.bonus = bonus
    def get_pay(self):
        payment = (self.wage*self.hours)+self.bonus
        return (payment)
    def __str__(self):
        string = self.name + " works on a contract of "+ str(self.hours) +" hours at " + str(self.wage) +"/hour and receives a bonus commission of "+ str(self.bonus) +". Their total pay is " + str((self.wage*self.hours)+self.bonus) + "."
        return string
    
class ContractCommisionSalary(SalaryMan):
    def __init__(self, name, salary, contracts, commision):
        super().__init__(name,salary)
        self.salary = salary
        self.contracts = contracts
        self.commision = commision
    def get_pay(self):
        return self.salary + (self.contracts*self.commision)
    def __str__(self):
        string = self.name + " works on a monthly salary of "+ str(self.salary) +" and receives a commission for "+ str(self.contracts) +" contract(s) at "+ str(self.commision) +"/contract. Their total pay is " + str(self.salary + (self.contracts*self.commision)) + "."
        return string
    
class ContractCommisionWage(Wage):
    def __init__(self, name, wage, hours, contracts, commision):
        super().__init__(name,wage, hours)
    
        self.contracts = contracts
        self.commision = commision
    def get_pay(self):
        return (self.wage*self.hours) + (self.contracts*self.commision)
    def __str__(self):
        string = self.name + " works on a contract of "+ str(self.hours) +" hours at " + str(self.wage) +"/hour and receives a commission for "+ str(self.contracts) +" contract(s) at "+ str(self.commision) +"/contract. Their total pay is " + str((self.wage*self.hours) + (self.contracts*self.commision)) + "."
        return string
    
# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = SalaryMan('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Wage('Charlie',25,100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = ContractCommisionSalary('Renee',3000, 4, 200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = ContractCommisionWage('Jan',25,150,3,220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = BonusCommisionSalary('Robbie', 2000, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = BonusCommisionWage('Ariel',30,120,600)
