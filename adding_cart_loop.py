# using for loop items adding to the cart


# cart = []
# n = int(input(f'Enter the number of item  you want add to the cart: '))
# for x in range(n):
#     item = input(f'Enter an item to the cart: ')
#     cart.append(item)
#     print(cart)

# using while loop items adding to the cart
cart = []

while True:
    choice = input(( f' Do you want to add the item to cart? : '))
    if choice   == 'yes':
        item = input(f'Enter an item to the cart: ')
        cart.append(item)
        print(f' Current cart  content are :  {cart}')
    else:
        print(f' exit from the adding cart item ')
        break

