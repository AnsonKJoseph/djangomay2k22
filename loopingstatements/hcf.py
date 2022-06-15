# # find the hcf or gcd of the numbers num1 and num2



# num1=15                                 #7th video (27-05-22)
# num2=35
# hcf=1                                     # here we given 1 because 1 is the common factor of all
# limit=num1 if num1<num2 else num2         # here we find limit to determine the smallest value among num1 and num2
# for i in range(2,limit+1):
#     if num1%i==0 and num2%i==0:
#         hcf=i
# print(hcf)

#
num1=15
num2=60
num3=45
hcf=1
limit=0
if num1<num2 and num1<num3:
    limit=num1
elif num2<num1 and num2<num3:     # python inbuilt function for finding min is (limit=min(num1,num2,num3)
    limit=num2
elif num3<num1 and num3<num2:
    limit=num3

for i in range(2,limit+1):
    if num1%i==0 and num2%i==0 and num3%i==0:
        hcf=i
print(hcf)