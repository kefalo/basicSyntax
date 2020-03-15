"""
Object Oriented Programming
###Creating your own methods###
"""


class Car(object):
    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def info(self):
        print("Make of the car: " + self.make)
        print("Model of the car: " + self.model)


c1 = Car('BMW', '520D')
print(c1.make, c1.model, c1.wheels)
# print(c1.info())

c2 = Car('Benz', '330ci')
print(c2.make, c2.model, c2.wheels)
# print(c2.info())

print(Car.wheels)
