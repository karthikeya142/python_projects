import json
import os.path

from file_handling.reading_usr_data import read_user_data


def delete_user_data(name):
    if not os.path.exists("user_data.json"):
        print("No user data found!")
        return
    with open("user_data.json",'r') as file:
        user_list = json.load(file)
        file.close()
    user_found = False
    for user_data in user_list:
        if user_data['name'] == name:
            user_list.remove(user_data)
            user_found = True
            break
    if not user_found:
        print("User Not Found")

    with open('user_data.json','w') as file:
        json.dump(user_list,file)
        print("User data deleted successfully")

delete_name = input("Enter name which you want  delete: ")
delete_user_data(delete_name)
read_user_data()

#
# edit_name = input("Enter name which you want add data for: ")
# edit_user_data(edit_name)
# def delete_user_data(name):
#     if not os.path.exists("user_data.json"):
#         print("No user data found")
#         return
#     with open('user_data.json','r') as file:
#         user_list =json.load(file)
#     user_found = False
#     for user_data in user_list:
#         if user_data['name'] == name:
#             user_list.remove(user_data)
#             user_found = True
#             break
#
#     if not user_found :
#         print("User not found")
#
#     with open("user_data.json",'r') as file:
#         json.dump(user_list,file)
#         print("User data deleted successfully")
