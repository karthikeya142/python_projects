#In Python, a class method is a method that is bound to the class and not the instance of the class.
# Class methods can modify class state that applies across all instances of the class.
# They are marked with the @classmethod decorator. Class methods take cls as their first parameter,
# which represents the class itself, whereas instance methods take self as their first parameter,
# which represents the instance of the class.

class Student():
    # clss variabe
    category = "student"

    @classmethod
    def info(cls):
        print(f"this is a method of class {cls.category} ")

Student.info()

