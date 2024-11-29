# for x in range(10):
#     print(x)
#     print("Karthikeya!")
#
# print("hi karthik!")

# loooping through the list

# fruits = ['apple','banana','mango','orange','dates','papaya','pineapple']
# for x in fruits:
#     print(x)

#looping through a Dictionary

people = {"karthik":23, "hari":20, "vikas":24}
for x in people:
    print(x)


#while loop
#While Loop is used to execute a block of statements repeatedly until a given condition is satisfied.
#When the condition becomes false, the line immediately after the loop in the program is executed.
counter =0
while counter<=10:
    print(counter)
    counter = counter + 1

#Python is used to bring the control out of the loop when some external condition is triggered.
# break statement is put inside the loop body (generally after if condition).
counter =11
while counter<=20:
    print(counter)
    if counter == 15:
        break
    counter = counter + 1