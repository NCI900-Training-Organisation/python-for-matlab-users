
'''
* Class: A blueprint for creating objects (instances). It defines a set of attributes (variables) 
and methods (functions) that the created objects will have.

* Object: An instance of a class. It is a collection of data (attributes) and methods that operate 
on the data.
'''

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # destructor
    def __del__(self):
        print(f" {self.make} object destroyed.")

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

# Creating an object (instance) of the class
car1 = Car("Toyota", "Camry", 2020)
car1.display_info()  

car2 = Car("Jeep", "Wrangler", 2019)
car2.display_info()  
