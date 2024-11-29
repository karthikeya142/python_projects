def print_arrows (n):
    total_rows = (n * 2) - 1
    for i in range(n):
        if i == 0 :
            print("*")
        elif i == 1:
            print("* *")
        elif i == n - 1:
            print("* "*n)
        else: print("*" + ' '*(2*i-1) + '*')
    for i in range ( n - 2, -1, -1):
            if i ==0 :
                print("*")
            elif i == 1 : print("* *")
            else: print("*" + ' '*(2*i-1) + '*')

n = int(input( "Enter a Number: "))

print_arrows(n)