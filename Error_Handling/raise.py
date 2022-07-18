# age=int(input("Enter age: "))
#
# if (age<18):
#     raise Exception("not eligible for taking booster dose")
# else:
#     print("eligible")




phone_num=input("Enter phone number: ")
if len(phone_num)!=10:
    raise Exception("Invalid phone number")
else:
    print("Valid")