x = float(input('Enter a number'))
y = float(input('Enter value by which you want to divide the number'))

def divide(*args):
    try:
        result = x /y

    except ZeroDivisionError:
        print("Cannot divide a number by zero ")
        return 0
    else:
        print(result)
    finally:
        print("no matter what make do ")

divide(x, y)