class Parent():
    def __init__(self):
        self.balance = 50000
    def display_balance(self):
        print(f"Parents's balance is {self.balance}")
class Child(Parent):
    pass
mike = Child()
mike.display_balance()
