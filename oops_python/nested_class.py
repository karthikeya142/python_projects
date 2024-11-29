#Certainly! Nested classes, or inner classes, are classes defined within another class.
# They are used to logically group classes that are only used in one place,
# to encapsulate and organize code better.

class Car():
    def __init__(self,brand):
        self.brand = brand
        self.steering_object = self.Steering()
    @staticmethod
    def Drive():
        print("Drive")
    class Steering():
        @staticmethod
        def rotate():
            print("Rotate")
car = Car("Roles")
car.Drive()

steering = car.steering_object
steering.rotate()