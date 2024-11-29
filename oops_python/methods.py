#writing metods
class Product():
    #quantity =300

    def __init__(self,name,price, discount_price):

        self.name = name
        self.price = price
        self.discount_price = discount_price

    def summer_discount(self, price, discount_percent):
        self.price = price
        self.discount_price = discount_percent
        total_price = price - (price * discount_percent / 100)
        return total_price

# Product1= Product("Laptop", 500)
# print(Product1.price)
#
# # let's call the method on object here
# Product1.summer_discount(10)
# print(Product1.price)
p1 = Product("Mobile", 5000, 10)
print(p1.price)
obj = p1.summer_discount(1000, 10)
print(obj)
# print(f'discount price of {p1.price}')
#
# p2 = Product("T-shirt","100")
# print(p2.name, p2.price)
# p2.summer_discount(10)
# print(f'discount price of {p2.price}')

#
#
#
# class Product:
#     quantity = 200
#
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     def summer_discount(self, discount_percent):
#         self.price = self.price - (self.price * discount_percent / 100)
#
#
# product1 = Product("Laptop", 500)
# print(product1.price)
#
# # let's call the method on object here
# product1.summer_discount(10)
# print(product1.price)
