
def save_user_data():
    name = input("Enter your Name: ")
    email = input("Enter your Email: ")
    contact = input("Enter Contact: ")

    usr_data = f"Name: {name}\nEmail: {email}\nContact: {contact}\n"
    with open('usr-data.txt','a') as file:
        file.write(usr_data)

def read_user_data():
    with open('usr-data.txt','r') as file:
        print(file.read())
save_user_data()
read_user_data()