#q1 2 => 2+22 = 24
#   3 => 3+33+333 = 369
#   4 => 4+44+444+4444 = 4936

num=3                           # 7th video (27-05-22)
i=1
pattern=""
sum=0
while(i<=num):
    pattern=pattern+str(num)
    sum=sum+int(pattern)
    i+=1
print(sum)



