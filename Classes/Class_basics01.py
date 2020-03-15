"""
Object Oriented Programming
Basics of Python OOP - Exercise #01
"""


class Car(object):
    def __init__(self, make, model):
        self.make = make
        self.model = model


c1 = Car('bmw', '520D')
# c1 is instance created from class Car, which is expecting value for 'make'
#  c1.make
print(c1.make, c1.model)

c2 = Car('Audi', 'S5')
print(c2.make, c2.model)
