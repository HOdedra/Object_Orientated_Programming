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
    raise_amt = 1.10
    
    #we need to implement an init because we have added prog_lang
    #therefore in order to add we must create an init method
    def __init__(self, first, last, pay, prog_lang):
        #super refers to the parent base class
        #is says call the parent(super) and runs it init
        super().__init__(first,last,pay)
        self.prog_lang = prog_lang
        
        
        

dev_1 = Developer('Corey', 'Schafer', 50000, 'Python') 
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

"""
what happened here was when we instantiated our developers
python looks in our developer class for the init method.
it doesnt find it there --> it walks up chain of inheritance to find what it is looking for
this is know as method resolution order

"""

print(dev_1.email)
print(dev_1.prog_lang)

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

#viewing method resolution order
print(help(Developer))      





