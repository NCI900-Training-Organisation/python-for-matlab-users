
'''
Encapsulation is the concept of restricting access to certain details of an object and only 
exposing a controlled interface. This is done using public and private attributes and methods.

Public members: Can be accessed directly.
Private members: Indicated by a leading underscore (e.g., _attribute). These are intended to be 
treated as internal and should not be accessed directly outside the class.

Variable and method names signals that they are intended for internal use (i.e., private), but Python
does not enforce this (unlike c or c++).
'''


class Account:

    # constructor 
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance  # private variable (convention)

    def deposit(self, amount):
        self._balance += amount

    def get_balance(self):
        return self._balance

# Creating an object
acc = Account("John", 1000)
acc.deposit(500)
print(acc.get_balance())  # Output: 1500
