# lst=[1,2,3,4]

# squares=[s**2 for s in lst]
# print(squares)

# squares=list(map(lambda s:s**2,lst))
# print(squares)

lst=[10,2,30,4]

# if map < 5 num-1 , if map > 5 num+1

# num=[num+1 if num>5 else num-1 for num in lst]
# print(num)
#
# num=list(map(lambda n:n+1 if n>5 else n-1,lst))
# print(num)

lst=[1,2,3,4,78,34,57]

gt_ten=list(filter(lambda n:n>10,lst))
print(gt_ten)

from functools import reduce

max_num=reduce(lambda n1,n2:n1 if n1>n2 else n2,lst)
print(max_num)