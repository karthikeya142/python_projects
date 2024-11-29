# map function in python it is built in function
# which means its actually predefine function in python
# it takes allows iterable list
# numbers = [1,2,3,4,5,6]
# def square(x):
#     return  x*x
# #normal loop using
# # for number in numbers:
# #     print(square(number))
#
# #now using map function
# new_list = list(map(square, numbers))
# print(new_list)
import struct
from re import split

# using map() different ways

# numbers = ['1','2','3','4','5','6']
# print(numbers)
# new_list = list(map(int, numbers))
# print(new_list)


#e-cart shoping prices on discount

# prices =[100,200,300,400,500]
# new_prices = list(map(lambda x: x-x*5/100, prices))
# print(new_prices)


# names = ['karthik', 'vikas','govardhan','sanjeev']
# new_list=list(map(str.upper, names))
# print(new_list)

# celsius to fahrenheittemparature using map
#farhenheit(°F)= Temparature in degree celsius (°C) * 9/5)+32

# celsius_temparature =[10,25,32,42,55]
# fahrenheit_temparature =list(map(lambda c: (c *9/5)+32, celsius_temparature))
# print(fahrenheit_temparature)

# Extracting initails from names

# names =['karthik kumar', 'vikas reddy', 'sanjeev reddy','govardhan paraku']
# for name in names:
#     name.capitalize()
#     print(name.split()[0][0].capitalize() + name.split()[1][0].capitalize())

# Extracting initails from names using map function
# names =['karthik kumar', 'vikas reddy', 'sanjeev reddy','govardhan paraku']
# initails = list(map(lambda name: "".join([n[0]for n in name.split()]).capitalize(), names))
# print(initails)


#revering the list using map function

names = ['karthik kumar', 'vikas reddy', 'sanjeev reddy', 'govardhan paraku']
reverse_names = list(map(lambda name:name[::-1],names))
print(reverse_names)
