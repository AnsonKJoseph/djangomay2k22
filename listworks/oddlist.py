# print odd list from list

list=[10,11,12,13,14,15,16,17,18,19,20]
oddlist=[]
for num in list:
    if num%2!=0:
        oddlist.append(num)
print(oddlist)
oddlist.sort(reverse=True)    #  sorts list in descending order
print(oddlist)