# reading the data in a file

import  json
import os
def save_user_data_():
    user_list =[]
    while True:
        name = input("Enter name (or 'quit' to exit the programm: ")
        if name == 'quit':
            break
        email = input("Enter Email: ")
        contact = input("Enter Contact: ")

        # creating a dictinory
        usr_data ={
            "name":name,
            "email":email,
            "contact":contact
        }
        user_list.append(usr_data)
    if os.path.exists('user_data.json') :
        with open('user_data.json','r') as file:
            exsting_data = json.load(file)
            user_list.extend((exsting_data))
    with open("user_data.json", "w") as file:
        json.dump(user_list,file)
        print(f'User data saved Successfully')
        file.close()


def read_user_data():
    if os.path.exists("user_data.json"):
        with open("user_data.json", "r") as file:
            user_list = json.load(file)
            for user_data in user_list:
                print("Name:", user_data["name"])
                print("Email:", user_data["email"])
                print("Contact:", user_data["contact"])
                print("")
    else:
        print("No User data found")
        return



#save_user_data_()
read_user_data()