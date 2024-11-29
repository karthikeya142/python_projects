# # to calculate monthly emi
# # formula to calcuate emi is : P X R (1+R)^N / [(1+R)^N-1]
# def emi_calculater(principal, rate, time):
#     r = rate/12/100
#     emi = (principal*r*(1+r)**time) / ((1+r)**time - 1)
#     return emi
#
# print(emi_calculater(80000, 6, 24))

#recursion method

# def hello():
#     print("hello\n")
#     hello()
#
# hello()

#recusrion using factorial of a number
# def factorial(N):
#     if N ==1:
#         return 1
#     else: return N * factorial(N-1)
# print(factorial(1))


# passing  multiple variables  to  the length positional  arguments
def arguments(*kt):
    sum = 0
    for n in values:
        sum = sum + n
    return sum
values = []
# while True:
#     print("enter number of entries: ")
#     n = int(input())
#     for i in range(n):
#         x = int(input("enter values here: "))
#         values.append(x)
#         print("value added is ", values)
#     h = arguments(values)
#     print(h)
#     break


print("enter number of entries: ")
n = int(input())
for i in range(n):
    x = int(input("enter values here: "))
    values.append(x)
    print("value added is ", values)
    h = arguments(values)
    print(h)

