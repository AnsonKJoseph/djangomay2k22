from Blog_practice.models_p import users
# print(users)

# authentication/login

username="akhil"
password="Password@123"


# for user in users:
#     if user["username"]==username and user["password"]==password:
#         print("Login Successful")
#         break
# else:
#     print("Invalid Details")

auth=[user for user in users if user["username"]==username and user["password"]==password]
if auth :
    print("Login Successful")
else:
    print("Invalid Details")
