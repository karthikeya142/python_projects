class Calculate():
    def add(self,a,b):
        return a+b

    def sub(self,a, b):
        return a - b

    def mul(self,a, b):
        return a * b

    def div(self,a, b):
        if b == 0:
            raise   ValueError("ZeroDivision Error")
        return a / b