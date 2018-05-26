"""
Subclasses and inheritance
this allows us to inherit attributes and methods from a parent class
we can create subclasses without affecting parent class
we can make managers/ developers
"""

class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        
class Developer(Employee):
    pass

dev_1 = Developer('Corey', 'Schafer', 50000)#'Python'
dev_2 = Developer('Test', 'Employee', 60000) #'Java'

"""
what happened here was when we instantiated our developers


"""

print(dev_1.email)
print(dev_1.email)

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

      
