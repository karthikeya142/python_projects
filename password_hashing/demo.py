import  bcrypt
password = b'karthikeya'
hash=bcrypt.hashpw(password,bcrypt.gensalt())
print(hash)

enter_passwd =input("enter password to login: ")
enter_passwd = bytes(enter_passwd,encoding ='utf-8')
if bcrypt.checkpw(enter_passwd,hash):
    print("Login successfull")
else:
    print("Invalid Password")