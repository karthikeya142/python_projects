#Multiple inheritance is a feature of some object-oriented programming languages, including Python,
# where a class can inherit attributes and methods from more than one parent class.
# This can be useful for combining behaviors and properties from multiple sources into a single class.
# However, it can also introduce complexity,
# particularly with the potential for method resolution order (MRO) issues.
# class A:
#     def method_A(self):
#         print("method A")
# class B:
#     def method_B(self):
#         print("method B")
# class C(A,B):
#     def method_C(self):
#         print("method C")
# cobject = C()
# cobject.method_A()
# cobject.method_B()
# cobject.method_C()

class Product():

    def __init__(self, name, price):
        self.price = price
        self.name = name
    def get_data(self):
        self.name = input("Enter the name of the product: ")
        self.price = int(input("Enter the price of the product: "))
    def put_data(self):
        print(self.name)
        print(self.price)
class warranty():
    def __init__(self, warranty_years):
        self.warranty_years = warranty_years
    def get_warranty(self):
        self.warranty_years = input("Enter the years of warranty: ")
class Electranics(Product,warranty):
    def __init__(self, name, price, warranty_years):
        Product.__init__(self, name, price)
        warranty.__init__(self, warranty_years)

Electranic_product = Electranics("","","")
Electranic_product.get_data()
Electranic_product.put_data()
Electranic_product.get_warranty()



# p1 = Product("","")
# p1.get_data()
# p1.put_data()





