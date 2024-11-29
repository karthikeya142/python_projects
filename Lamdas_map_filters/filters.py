# odd_num =[]
# evn_num =[]
# for number in range(100):
#     if number%2==1:
#         odd_num.append(number)
#     else:
#         evn_num.append(number)

# print(f'even_numbers: {evn_num}')
# print(f'odd_numbers: {odd_num}')

numbers = [1,2,3,4,5,6,7,8,9]

# def odd(x):
#     if x%2==1:
#         return x
# odd_numbers =list(filter(odd,numbers))
# print(odd_numbers)

# we can write on the lambda function
odd_numbers =list(filter(lambda x: x%2==1,numbers))
print(odd_numbers)