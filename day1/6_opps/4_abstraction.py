
'''
Abstraction involves hiding the complex implementation details of a class and only exposing a 
simplified interface. Python uses abstract classes and abstract methods to achieve this.

An abstract class cannot be instantiated directly, and it typically contains abstract methods 
that must be implemented by subclasses.

'''

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

# Circle and Square must implement the area method
circle = Circle(5)
square = Square(4)
print(circle.area())  # Output: 78.5
print(square.area())  # Output: 16
