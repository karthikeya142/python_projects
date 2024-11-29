# a = int(input('Enter a value of A: '))
# b = int(input("Enter a value of B: "))
# if a>30:
#     if b>40:
#         print(" A is graethan 30 & B is greather 40 ")
#     else:
#         print('B is not greathan 40 , But A is greathan 30')
# else:
#     print("A is not Greaterthan 30")

age = int(input( "Enter your age :"))
if age>=18:
    score = int(input("Enter your exam score: "))
    if score>40:
        print("You meet both age and score criteria, You are qualified")
    else:
        print(" You meet the age criteria, but do not meet the score  criteria")
else:
    print("you do not meet the age criteria, please try when you above 18")

