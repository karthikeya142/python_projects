#In Python, a static method is a method that belongs to a class rather than an instance of a class.
# Static methods do not modify the state of an instance or class and do not take self or cls as their first parameter.
# They are defined using the @staticmethod decorator.

#Comparing with Class Methods and Static Methods
#Instance Methods: Operate on an instance of the class using self.
#Class Methods: Operate on the class itself using cls and are marked with the @classmethod decorator.
#Static Methods: Do not operate on an instance or class directly and are marked with the @staticmethod decorator.
# They do not take self or cls as their first parameter.



class student():

    @staticmethod
    def add(a,b):
        print (a+b)
student.add(2,4)

#another example static method

class  circle():
    @staticmethod
    def area(r):
        return 3.14*r*r
    @staticmethod
    def circumference(r):
        return 2*3.14*r

r = int(input("enter the radius of the circle "))

print("Area of the circle:", circle.area(r))
print("Circumference of the circle:", circle.circumference(r))
#
# class TemperatureConverter:
#     @staticmethod
#     def celsius_to_fahrenheit(celsius):
#         return (celsius * 9/5) + 32
#
#     @staticmethod
#     def fahrenheit_to_celsius(fahrenheit):
#         return (fahrenheit - 32) * 5/9
#
# # Call static methods without creating an instance
# celsius = 25
# fahrenheit = TemperatureConverter.celsius_to_fahrenheit(celsius)
# print(f"{celsius}°C is {fahrenheit}°F")  # Output: 25°C is 77.0°F
#
# fahrenheit = 77
# celsius = TemperatureConverter.fahrenheit_to_celsius(fahrenheit)
# print(f"{fahrenheit}°F is {celsius}°C")  # Output: 77°F is 25.0°C
