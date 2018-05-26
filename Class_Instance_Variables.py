"""
init method is initialized everytime an instance is created
first/last/email etc are instance variables
Class variables are the same for each instances. what data would we like to share amongst everyone
e.g. pay rise!
when we acces them we must do so through an instance or the class itself
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

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1.pay) #50,000
emp_1.apply_raise() #*1.04
print(emp_1.pay)#52,000

"""
Why can we access these variables through our instance?
"""
print(Employee.raise_amt) #1.04
print(emp_1.raise_amt)#1.04
print(emp_2.raise_amt)#1.04

#more proof
#print name space of the instance
print(emp_1.__dict__)
"""
{'first': 'Corey', 'last': 'Schafer', 'email': 'Corey.Schafer@email.com', 'pay': 52000}
1.04 isn't in the name_space
"""
print(Employee.__dict__) #however it is in the Employee class

#we could also change raise_amt just for emp_1
emp_1.raise_amt = 1.05
print(emp_1.__dict__) #1.05 would be in this name space






