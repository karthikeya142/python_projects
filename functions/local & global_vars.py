# calling global  varible
name = 'karthikeya'

# calling local varible
# we declare inside of a function trested as alocala varibale
def karthik():
    name = 'sanjeeva'
    return name

print(f' calling  global varibele : {name}')

print( f' calling local varible :  {karthik()} ')

# accessing global values inside a function

first = "karthiksanju"
def name():
    print(first)
    # inside function calling the global varibalen first

name()
