"""
Inheritance
"""
class Car(object):
    def __init__(self):
        print("You just created the car instance")

    def drive(self):
        print("Car started...")

    def stop(self):
        print("Car stopped")


class BMW(Car):

    def __init__(self):
        # Car.__init__(self)
        # another method of calling the __init__(self) method of the Car class
        super().__init__()
        print("You just created the BMW instance")


c = Car()
c.drive()
c.stop()

b = BMW()
b.drive()
b.stop()
