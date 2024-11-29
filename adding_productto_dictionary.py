products = {'phone':100,'laptop':200,'headphone':300,'pen':400,'book':500,'alexa':600}
print(products)
# change the product price
price_change_product = input(f' enter product which you want change the product: ')
price_change =input(f' Enter new price for {price_change_product}')
products[price_change_product]=price_change
print(f' product price changed, here is list of product {products}')
#delite the product from the dictionary
# deleted_product = input(f"Enter the product to delete: ")
# del products[deleted_product]
# print(f" Product deleted, here is updated products {products} ")
# adding a new product to the dictionary

# product = input(f"Enter the product to check the price ")


# product = input("Enter the product to check the price: ")
# if product in products:
#     print(f"The price of {product} is {products[product]}")
# else:
#     print(f"{product} is not in the list.")


product = input(f"Enter the product to check the price ")
print(f' price of the {product} is {products[product]}:')
product in products
new_product =input(f" Enter product you want add: ")
new_product_price = input(f"Enter the price of {new_product}: ")
products[new_product]= new_product_price

print(f' product successfully added, Here is an updated products list: {products}')