num1=10
num2=120
num3=30
if num1>num2 and num1>num3:
    print("num1 is largest")
elif num2>num1 and num2>num3:
    print("num2 is largest")
elif num3>num1 and num3>num2:
    print("num3 is largest")
# else:
#     print("All are same ")
elif num1==num2 and num2==num3:
    print("All are same")


# Python inbuilt function for max and min value


largest=max(num1,num2,num3)
print(largest)


lowest=min(num1,num2,num3)
print(lowest)