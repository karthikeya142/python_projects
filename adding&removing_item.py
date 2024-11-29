products = ['phone','laptop','headphone','pen','book','alexa']

print(f'current list of items: {products}')
# asking to the user to remove a products

item_remove =input("Enter product to remove from the above list: ")
products.remove(item_remove)

# Displaying the entire list after removing  item
print(f'current list of items: {products}')

# asking to the user to adding  a products
item_adding =input('Enter product to adding from the list: ')

# whenever adding item in products will add end of the list
products.append(item_adding)

# whenever adding item in products will add we will give the index of the product of the list
#add_after =input(f'after which product do you want  place {item_adding} ')
#index = products.index(add_after)
#products.insert(index+1, item_adding)

# Displaying the entire list after adding  item
print(f'current list of items: {products}')


