# Father Mother Skilss
from abc import ABC, abstractmethod
class Father:
    def skills(self):
        print('Coding, Fishing')


class Mother:
    def skills(self):
        print('Cooking, cleaning')


class Child(Father, Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)


c = Child()
c.skills()

# Polymorphism
# What is polymorphism?

# Example Three: Polymorphism with inheritance
# Superclass
class Bird:
    def fly(self):
        print('Birds flies in the sky')


# derived class
class Eagle(Bird):
    def fly(self):
        print('Eagle flies at high altitude')


class Sparrow(Bird):
    def fly(self):
        print('Sparrow flies at low altitude')


# How we use polmorphism
def flight_test(bird):
    bird.fly()  # Run respective class method based on an object


# Create objects
eagle1 = Eagle()
sparrow1 = Sparrow()

# Call the flight test method with diffrent objects

flight_test(eagle1)
flight_test(sparrow1)

#Abstraction
#Abstract Class and interfaces
#Example four.
#define an abstract class
class Shape (ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
class Rectangle (Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2*(self.length + self.width)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Example usage
rect = Rectangle(5, 10)
print(f"Rectangle Area: {rect.area()}")
print(f"Rectangle Perimeter: {rect.perimeter()}")

circle = Circle(7)
print(f"Circle Area: {circle.area()}")
print(f"Circle Perimeter: {circle.perimeter()}")
    