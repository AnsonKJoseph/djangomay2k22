# num=10
# for i in range(2,num):
#     if num%i==0:
#         print("Not Prime")
#         break
# else:
#     print("Prime")


#          OR


num=10
flag=0
for i in range(2,num):
    if num%i==0:
        flag=1
        break
if(flag==0):
    print("Prime")
else:
    print("Not Prime")