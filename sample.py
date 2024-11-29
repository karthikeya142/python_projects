def arguments(*args):
    def add(*args):
        """Calculates the sum of the arguments and returns the result."""
        return sum(args)

    def sub(*args):
        """Calculates the difference of the first two arguments and returns the result.
        Assumes at least two arguments are provided."""
        if len(args) < 2:
            print("Subtraction requires at least two numbers.")
            return None
        return args[0] - args[1]

    def mul(*args):
        """Calculates the product of all arguments and returns the result."""
        product = 1
        for num in args:
            product *= num
        return product

    def div(*args):
        """Calculates the division of the first argument by the second and returns the result.
        Handles division by zero error."""
        if len(args) < 2:
            print("Division requires at least two numbers.")
            return None
        if args[1] == 0:
            print("Division by zero is not allowed.")
            return None
        return args[0] / args[1]

    values = []

    print("Enter number of entries: ")
    n = int(input())

    for i in range(n):
        try:
            x = float(input("Enter values here: "))
            values.append(x)
            print("Value added is ", values)
        except ValueError:
            print("Invalid input. Please enter numbers only.")

    # Move the infinite loop for user choice outside the input loop
    while True:
        print("Select one option:\n"
              "1. Add\n"
              "2. Subtract\n"
              "3. Multiply\n"
              "4. Division")
        user = int(input("Enter your choice = "))
        if user == 1:
            result = add(*values)
            if result is not None:
                print("Addition is ", result)
        elif user == 2:
            result = sub(*values)
            if result is not None:
                print("Subtraction is ", result)
        elif user == 3:
            result = mul(*values)
            if result is not None:
                print("Multiplication is ", result)
        elif user == 4:
            result = div(*values)
            if result is not None:
                print("Division is ", result)
        else:
            print("Choose a correct option")
        print()  # Add an empty line for better readability

# Call the function to start the program
arguments()











#
# #def add(*args):
#     """Calculates the sum of the arguments and returns the result."""
#     return sum(args)
#
# def sub(*args):
#     """Calculates the difference of the first two arguments and returns the result.
#     Assumes at least two arguments are provided."""
#     if len(args) < 2:
#         print("Subtraction requires at least two numbers.")
#         return None
#     return args[0] - args[1]
#
# def mul(*args):
#     """Calculates the product of all arguments and returns the result."""
#     product = 1
#     for num in args:
#         product *= num
#     return product
#
# def div(*args):
#     """Calculates the division of the first argument by the second and returns the result.
#     Handles division by zero error."""
#     if len(args) < 2:
#         print("Division requires at least two numbers.")
#         return None
#     if args[1] == 0:
#         print("Division by zero is not allowed.")
#         return None
#     return args[0] / args[1]
#
# def main():
#     values = []
#
#     try:
#         n = int(input("Enter number of entries: "))
#     except ValueError:
#         print("Invalid input. Please enter an integer.")
#         return
#
#     for i in range(n):
#         try:
#             x = float(input(f"Enter value {i+1}: "))
#             values.append(x)
#             print("Value added is ", values)
#         except ValueError:
#             print("Invalid input. Please enter numbers only.")
#             return
#
#     while True:
#         print("Select one option:\n"
#               "1. Add\n"
#               "2. Subtract\n"
#               "3. Multiply\n"
#               "4. Division\n"
#               "5. Exit")
#         try:
#             user = int(input("Enter your choice: "))
#         except ValueError:
#             print("Invalid input. Please enter a valid option.")
#             continue
#
#         if user == 1:
#             result = add(*values)
#             if result is not None:
#                 print("Addition is ", result)
#         elif user == 2:
#             result = sub(*values)
#             if result is not None:
#                 print("Subtraction is ", result)
#         elif user == 3:
#             result = mul(*values)
#             if result is not None:
#                 print("Multiplication is ", result)
#         elif user == 4:
#             result = div(*values)
#             if result is not None:
#                 print("Division is ", result)
#         elif user == 5:
#             print("Exiting the program.")
#             break
#         else:
#             print("Choose a correct option")
#         print()  # Add an empty line for better readability
#
# # Call the main function to start the program
# main()
#
