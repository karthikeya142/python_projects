#Multi-level inheritance is a type of inheritance where a class is derived from another derived class.
# This forms a chain of inheritance.
# For example, if class B is derived from class A, and class C is derived from class B

# class A:
#     def method_A(self):
#         print("method A")
# class B(A):
#     def method_B(self):
#         print("method B")
# class C(B):
#     def method_C(self):
#         print("method C")
# cobject = C()
# cobject.method_A()
# cobject.method_B()
# cobject.method_C()
#

class Product():

    def __init__(self, name, price):
        self.price = price
        self.name = name
        self.discount_price = None
    def get_data(self):
        self.name = input("Enter the name of the product: ")
        self.price = int(input("Enter the price of the product: "))
        if self.discount_price is not None:
            print(f"Discounted Price: {self.discount_price}")
        else:
            print("Discounted Price: Not applied")
    def summer_discount(self, discount_price):
        self.discount_price = self.price - (self.price * discount_percent / 100)
        return self.discount_price
    def put_data(self):
        print(self.name)
        print(self.price)
        # print(self.discount_price)
class warranty(Product):
    def __init__(self, warranty_years):
        self.warranty_years = warranty_years
    def get_warranty(self):
        self.warranty_years = input("Enter the years of warranty: ")
class mobile(warranty):
    def __init__(self, name, price, warranty_years, brand):
        Product.__init__(self, name, price)
        warranty.__init__(self, warranty_years)
        self.brand = brand

    def get_brand(self):
        self.brand = input("Enter the brand of the mobile: ")
    def put_brand(self):
        print(f"Brand: {self.brand}")
mobile_product = mobile("","","","")
mobile_product.get_data()
mobile_product.get_warranty()
mobile_product.get_brand()

mobile_product.put_data()
discount_percent = float(input("Enter the discount percentage: "))
print(f"Price after discount: {mobile_product.summer_discount(discount_percent)}")



















# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = float(price)
#         self.discount_price = None
#
#     def get_data(self):
#         self.name = input("Enter the name of the product: ")
#         self.price = float(input("Enter the price of the product: "))
#
#     def put_data(self):
#         print(f"Name: {self.name}")
#         print(f"Price: {self.price}")
#         if self.discount_price is not None:
#             print(f"Discounted Price: {self.discount_price}")
#         else:
#             print("Discounted Price: Not applied")
#
#     def summer_discount(self, discount_percent):
#         self.discount_price = self.price - (self.price * discount_percent / 100)
#         return self.discount_price
#
# class Electronics(Product):
#     def __init__(self, name, price, warranty_years):
#         super().__init__(name, price)
#         self.warranty_years = int(warranty_years)
#
#     def get_warranty(self):
#         self.warranty_years = int(input("Enter the years of warranty: "))
#
#     def put_warranty(self):
#         print(f"Warranty Years: {self.warranty_years}")
#
# class Mobile(Electronics):
#     def __init__(self, name, price, warranty_years, brand):
#         super().__init__(name, price, warranty_years)
#         self.brand = brand
#
#     def get_brand(self):
#         self.brand = input("Enter the brand of the mobile: ")
#
#     def put_brand(self):
#         print(f"Brand: {self.brand}")
#
# # Create an instance of Mobile
# mobile_product = Mobile("", 0, 0, "")
# mobile_product.get_data()
# mobile_product.get_warranty()
# mobile_product.get_brand()
#
# mobile_product.put_data()
# discount_percent = float(input("Enter the discount percentage: "))
# print(f"Price after discount: {mobile_product.summer_discount(discount_percent)}")
# mobile_product.put_warranty()
# mobile_product.put_brand()
