list=[1,2,3,4,5,6,7,8]
element=1
flag=0
for i in range(0,len(list)):
    if element==list[i]:
        flag=1
        break
print("Element found" if flag!=0 else "Element not found")