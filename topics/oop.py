from typing import Tuple,List,Union,Optional
class Person:
    def __init__(self, name: str, age: Optional[int]):
        self.name = name
        self.age = age

person1 = Person("Jessica",27)
person2 = Person("Jessica",67)
person2.age = 38

print(person2.age)

class Circle:
    pi = 3.14
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return self.pi * self.radius ** 2

circle = Circle(5)
print(f"circle aread = {circle.area()}")

#dealing with instance methods vs class methods

