from Blog_practice.models_p import users
# print(users)


def authenticate(**kwargs):
    username=kwargs.get("username")
    password=kwargs.get("password")
    user = [user for user in users if user["username"] == username and user["password"] == password]
    return user
print(authenticate(username="akhil",password="Password@123"))


