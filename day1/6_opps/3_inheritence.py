
'''
Inheritance allows one class to inherit the attributes and methods of another class. The new class 
(child or subclass) can add new attributes or methods or override existing ones.

Base Class (Parent Class): The class whose properties and methods are inherited.
Derived Class (Child Class): The class that inherits from the parent class.
'''

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

    def legs(self):
        print(f"{self.name} has four legs")

class Dog(Animal):  # Dog inherits from Animal
    def speak(self):
        print(f"{self.name} barks") # polymorphism

class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows")

# Creating objects of derived classes
dog = Dog("Buddy")
cat = Cat("Whiskers")
dog.speak()  
dog.legs() 
cat.speak() 
cat.legs() 
