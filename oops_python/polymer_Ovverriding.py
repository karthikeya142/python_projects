#Polymorphism is a key concept in object-oriented programming (OOP)
#that allows objects of different classes to be treated as objects of a common superclass.
# It is the ability to present the same interface for differing underlying forms (data types).
# Polymorphism in Python can be achieved through method overriding,
# method overloading (though Python does not support this natively), and operator overloading.

# class Food():
#     def type(self):
#         print("Food")
# class Fruit(Food):
#     def type(self):
#         print("Fruit")
#
# apple = Fruit()
# print(apple.type())




#instance method

#Instance methods are defined similarly to regular functions, but they take self as their first parameter.
# self refers to the instance on which the method is called.
# Through self, instance methods can access other methods and attributes of the same object.
class student():
    def __init__(self,name):
        # instance variable
        self.name = name
        # instane method
    def hello(self):
        print(f" hello my name is {self.name}")
    # instance method
    def name_length(self):
        return len(self.name)
s1 =student("karthik")
print(s1.hello())
print(s1.name_length())
