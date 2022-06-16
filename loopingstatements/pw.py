# num=123
# (1**3) + (2**3) + (3**3)
#  (1) + (8) + (27) = 36

num=2345
sum=0
while(num!=0):
    last_digit = num%10
    cube=last_digit**3
    sum=sum+cube
    num=num//10
print(sum)

# This program is applicable for only continuous numbers eg: 123,234,5678


