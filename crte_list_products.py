# adding list of products
products=[
    {"name":"laptop", "price":200, 'description': 'a good quality of laptop it has new features 16 GB of ram, 256gb of SSD and 1 TB of hdd'},
    {"name": "iQoo 6","price":100, 'description': "it has snapdragon 876"},
    {"name":'apple','price':500,"description":'india newest mobile'},
    {"name":"ipad", "price":300, 'description': 'a good quality of ipadit has new features 16 GB of ram, 256gb of SSD and 1 TB of hdd'},
    {"name": "bwm","price":800, 'description': "it has automatic sensor system"},
    {"name":'rrr','price':400,"description":'india newest rrr'},
    {"name": "Smartphone", "price": 600,"description": "A handheld device used for communication and browsing the internet."},
    {"name": "Laptop", "price": 1000, "description": "A portable computer that is easy to carry around."},
    {"name": "Headphones", "price": 50, "description": "A pair of earphones worn over the head to listen to music."},
    {"name": "Smartwatch", "price": 300,"description": "A wearable device used for fitness tracking and receiving notifications."},
    {"name": "Bluetooth speaker", "price": 100,"description": "A portable speaker that connects wirelessly to devices using Bluetooth technology."}
]
cart = []
while True:
    choice = input("Do you want continue  shopping?: ")
    if choice == "yes":
        print("Here is a list products and their prices: ")
        for index,product in enumerate(products):
            print(f"{index} : {product['name']}: {product['price']}: {product['description']}")
            # adding items to the cart
        product_id = int(input("Enter the id of  product do you want add cart:  "))
        if products[product_id] in cart:
            products[product_id]['quantity'] += 1
        else:
            products[product_id]['quantity'] =1
            cart.append(products[product_id])


        total = 0
        print(f'Current cart contents are {cart}')
        # calaculating total cart value

        for product in cart:

            print(f'{product["name"]} : ${product['price']} : {product["description"]} : Qty : {product['quantity']}')
            total = total + product['price'] * product['quantity']
        print(f' Cart total is : {total}')
    else:
        break

print(f'thak you, your final cart contents are {cart} ')
print(f' Cart total is : {total}')