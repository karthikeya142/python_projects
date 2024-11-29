class Product():

    def __init__(self, name, price):
        self.price =price
        self.name = name
    def get_data(self):
        self.name = input("Enter the name of the product: ")
        self.price = input("Enter the price of the product: ")
    def put_data(self):
        print(self.name)
        print(self.price)

p1 = Product("","")
p1.get_data()
p1.put_data()