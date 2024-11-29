# def products(**kwargs):
#     for key, value in kwargs.items() :
#         print(key+":"+value)
#
# products(name = "iphone", price = "8000")
# products(name = "ipad", price = "9000", discription = ' this is a ipad')
#



#very powerful and useful tool in Python since it allows programmers to modify the behaviour of a function or class.
# Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying i


# def decorator(func):
#     def wrapper(*args,**kwargs):
#         print("wrapper is up side")
#         func(*args,**kwargs)
#         print("wrapper is down side")
#     return wrapper
#
# @decorator
# def chacolate():
#     print("chacolate")
# @decorator
# def cake(name):
#     print("Cake "+name)
#
# chacolate()
# cake("apple")


#decorating functions returning values

def summer_discount_decorator(func):
    def wrapper(price):
        func(price)
        return  func(price/2)
    return wrapper
@summer_discount_decorator
def total(price):
    return price

print(total(100))