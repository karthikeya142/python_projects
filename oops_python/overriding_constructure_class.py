#Using the super function can help ensure that your class correctly inherits and initializes its parent class's properties.
# This is particularly useful if you have additional functionality or more complex inheritance hierarchies.
class Parent():
    def __init__(self):
        self.parent_balance = 50000
    def display_balance(self):
        print(f"Parent's balance {self.parent_balance}")

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.child_balance =  20000
    def display_balance(self):
        print(f" Childs's balance {self.child_balance + self.parent_balance}")

karthik = Child()
karthik.display_balance()