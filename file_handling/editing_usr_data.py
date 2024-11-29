# edit user data from a file
import json
import os
import reading_usr_data
def read_user_data():
    if  not os.path.exists("user_data.json"):
        print("No User data found")
        return
    with open("user_data.json", "r") as file:
        user_list = json.load(file)
        for user_data in user_list:
            print("Name:", user_data["name"])
            print("Email:", user_data["email"])
            print("Contact:", user_data["contact"])
            print("")

def edit_user_data(name):
    if not os.path.exists("user_data.json"):
        print("No user data found!")
        return
    with open("user_data.json",'r') as file:
        user_list = json.load(file)
        file.close()
    user_found = False
    for user_data in user_list:
        if user_data['name'] == name:
            name = input("Enter name")
            email = input("Enter Email")
            contact = input("Enter Contact")

            user_data['name']=name
            user_data['email']=email
            user_data['contact']=contact
            user_found = True
            break
    if not user_found:
        print("User Not Found")
        return

    with open('user_data.json','w') as file:
        json.dump(user_list,file)
        print("User data added successfully!")


edit_name = input("Enter name which you want add data for: ")
edit_user_data(edit_name)