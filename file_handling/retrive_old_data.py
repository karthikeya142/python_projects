# preserving old data in a file

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



save_user_data_()
