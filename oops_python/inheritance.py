#One of the core concepts in object-oriented programming (OOP) languages is inheritance.
# It is a mechanism that allows you to create a hierarchy of classes that share a set of properties
# and methods by deriving a class from another class. Inheritance ...
# Base class (superclass)

class Product():
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def get_data(self):
        self.name =input("Enter name of the product: ")
        self.price=input("Enter the price of product: ")
    def put_data(self):
        print(self.name)
        print(self.price)
class DigitalProduct(Product):
    def __init__(self,link):
        self.link = link
    def get_link(self):
        self.link =input("Enter the Product link: ")
    def put_link(self):
        print(self.link)
ebook =DigitalProduct("")
ebook.get_data()
ebook.get_link()
ebook.put_data()
ebook.put_link()

