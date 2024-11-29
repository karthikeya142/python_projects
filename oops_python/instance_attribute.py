#creating constucters and passing the values
class Product():
    #quantity =300

    def __init__(self,name,price):
        self.name = name
        self.price =price

p1 = Product("mobile","5000")
print(p1.name, p1.price)