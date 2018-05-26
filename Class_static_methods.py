"""
Classmethods and static methods
for classmethods we are working with the class and not just the instance
therefore we use 'cls'
"""

class Employee:

    num_of_emps = 0
    
    raise_amt = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
        
        #example where we use Employee instead of self for a class variable
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt) #this could also be Employee.raise_amt
        
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt = amount
    
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1.pay) #50,000
emp_1.apply_raise() #*1.04
print(emp_1.pay)#52,000

Employee.set_raise_amt = 1.05

"""
class methods can be used as alternative constructors
different ways of creating objects
"""
#convert these into objects
#can do this manually but there are easier methods
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.first)












