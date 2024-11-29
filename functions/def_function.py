# #defining a functions
# # def hello():
# #     name = input("enter your name: ")
# #     print(f' hello {name}')
# #
# # hello()
# #
# # def add(a, b):
# #     print(a)
# #     print(b)
# #     print(a+b)
# #
# # add(33, 55)
# # print("helo")
# # add(80,140)
#
# default parameters
# def area(radius, pi=3.15):
#     reslut =(pi*radius*radius)
#     return reslut
#
# def cost(calculated_area, cost_per_sqm):
#     total_cost = calculated_area*cost_per_sqm
#     return total_cost

# calculated_area = area(10, )
# tc = cost(calculated_area, 2)
# print(tc)

# calling  a function in another function
# print(cost(area(10),2))

# making a function  return multiple values
# def circle(r):
#     area = 3.14*r*r
#     cirecuference= 2*3.14*r
#     return area, cirecuference
# a, b =circle(10)
# print(f' area of the circle  is {a}  and circumference of the cirlce is {b}')


# passing list to function
# scores =[1,2,3,4,5,6,7,8,9]
# def add(numbers):
#     total =0
#
#     for number in numbers:
#         print(number)
#         total = total + number
#     return total
#
# result = add(scores)
# print(result)


# removing a duplicates in a list using function

def remove_duplicates(numbers):
    return list(set(numbers))
    # new_list =[]
    # for number in numbers:
    #     if number not in new_list:
    #         new_list.append(number)
    # return new_list
ids = [1,2,3,4,5,6,7,8,9,0,4,3,1,2,4,6,5,11,22,3,44,44,5555,66,0]

print(remove_duplicates(ids))









# def maths():
#     a = int(input("enter a number : "))
#     b = int(input("enter a number : "))
#     def add():
#         print(f"additon of {a} and {b} is {a + b}")
#     def sub():
#         print(f'subtraction of {a} and {b} is {a - b}')
#
#     add()
#     sub()
#
# maths()

# def add(a,b):
#     print("Addition is ", a+b)
# def sub(a,b):
#     print("subtraction is ", a-b)
# def mul(a,b):
#     print("Multiplication is ", a * b)
# def div(a,b):
#     print("Division is ", a / b)
# while True:
#     a = int(input("enter number a= "))
#     b = int(input("enter number b= "))
#     print("select one option\n"
#           "1. add\n"
#           "2.subtraction\n"
#           "3.multiplication\n"
#           "4.division")
#     user = int(input("enter your choice ="))
#     if user == 1:
#         add(a,b)
#     elif user ==2:
#         sub(a,b)
#     elif user == 3:
#         mul(a,b)
#     elif user == 4:
#         div(a,b)
#     else: print("choose correct option")
#
#









