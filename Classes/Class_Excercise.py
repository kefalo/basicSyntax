"""
Class Excercise
############################
Create a class Fruit
define 3 methods in this class
__init__()
nutrition()
fruit_shape()
print anything you like in this classes
#############################


Create one more class (any fruit name)

This class should inherit from the Fruit class created above, this will become the child class
and "Fruit" will be referred as parent class to this class.
Define 3 methods in this class
__init__()
nutrition()
color()
print anything you like in this methods
"""

class Fruit():
    def __init__(self):
        #super().__init__()
        print("Creation of the Fruit class instance")

    def nutrition(self):
        print("Puno vitamina")

    def fruit_shape(self):
        print("triangle shape")

class Jagoda(Fruit):

    def __init__(self):
        #super(Fruit, self).__init__()
        print("Creation of the new Jagoda class instance")
        #super().nutrition()
        #super().fruit_shape()

    def nutrition(self):
        print("Slatka")
        #super().fruit_shape()

    def fruit_Color(self):
        print("Crvena")
        
        

f = Fruit()
f.nutrition()
f.fruit_shape()

j = Jagoda()
j.nutrition()
j.fruit_Color()
j.fruit_shape()