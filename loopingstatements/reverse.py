# reverse 123


# num=123
# while(num!=0):
#     last_digit = num%10
#     print(last_digit,end="")
#     num=num//10


num=123                            #  6th video (26-05-22)
res=""
while (num!=0):
    last_digit=num%10
    res=res+str(last_digit)
    num=num//10
print(res)

