from typing import Tuple, List, Union, Optional


class Person:
    def __init__(self, name: str, age: Optional[int]):
        self.name = name
        self.age = age


person1 = Person("Jessica", 27)
person2 = Person("Jessica", 67)
person2.age = 38

print(person2.age)


class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.pi * self.radius ** 2


circle = Circle(5)
print(f"circle aread = {circle.area()}")


# dealing with instance methods vs class methods

class Dog:
    defaultName = "puppy"  # class variable

    def __init__(self, dogName: str = None):
        if dogName is None:
            self.dogName = Dog.defaultName
            return
        self.dogName = dogName  # instance variable

    def burk(self):
        print(f"burking dog {self.dogName}")  # here burk is instance method which means it can be accessed by self


dogg = Dog()
dogg.burk()


class MathOperation:
    classVariable = 'something to show '

    @classmethod
    def add(cls, a, b): return a + b

    @staticmethod
    def multiply(a, b): return a * b

    def instanceMethod(self, name=None):
        if name is None: name = MathOperation.classVariable
        return name


mathOperation = MathOperation().multiply(223, 22)
mathOperation2 = MathOperation().add(223, 22)
mathOperation3 = MathOperation().instanceMethod('jessica')

print(mathOperation)
print(mathOperation2)
print(mathOperation3)


# difference between class methdos and instance methods, so class methods you can access
# through the class initilization while instance you have to previous state the initialization
# so then after that you can take the value


class Rectangle:
    def __init__(self, width, height):
        self._width, self.height = width, height

    @property
    def width(self):
        return self._width

    @property
    def area(self):
        return self._width * self.height

    # setting setter on width property

    @width.setter
    def width(self, value):
        if value >= 5:
            self._width = value * 5
        else:
            raise ValueError(f"Value should be greater than 5 or ")


rect = Rectangle(78, 5)
print(rect.area)  # Output: 20
rect.width = 6
print('react ared ', rect.area)  # Output: 30
"""
this code version has an error of RecurionError  can you identify why ? 
class Rectangle:
    def __init__(self,width,height):
        self.width,self.height = width,height
    @property
    def width(self):
        return self.width
    @property
    def area(self):
        return self.width * self.height
    #setting setter on width property

    @width.setter
    def width(self,value):
        if value >= 5:
            self.width = value*5
        else: raise ValueError(f"Value should be greater than 5 or ")

rect = Rectangle(78, 5)
print(rect.area)  # Output: 20
rect.width = 6
print('react ared ',rect.area)  # Output: 30
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass
import math


class Shape(ABC):
    @abstractmethod
    def area(self): pass # abstract method to be implemented where inherited

    @abstractmethod
    def perimiter(self): pass # abstract methods to be implemented where inherited


@dataclass #this automatically implements __init__ , __repr__  and __eq__
class Rectangle(Shape):
    width: float
    height: float
    def area(self):
        return self.width * self.height
    def perimiter(self):
        return 2 * (self.width + self.height)
@dataclass
class Circle(Shape):
    radius: float
    def area(self):
        return math.pi * self.radius ** 2
    def perimiter(self):
        return 2 * math.pi * self.radius


class Square(Circle):
    def __init__(self,length):
        super().__init__(length)
