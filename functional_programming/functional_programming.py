from functools import reduce

# map
# filter
# reduce

# these are inbuilt functions

# print sqaures of the nums in list

lst=[10,2,30,4]
# using list comprehension

# squares=[n**2 for n in lst]
# print(squares)

# using map function

# squares=list(map(lambda n:n**2,lst))
# print(squares)

# print cubes of nums in list

# cubes=list(map(lambda n:n**3,lst))
# print(cubes)


# print num+1 if num>5 and num-1 if num<5

# using list comprehension

# lst=[10,2,30,4]
# num_out=[num-1 if num<5 else num+1 for num in lst ]
# print(num_out)

# using map

# lst=[10,2,30,4]
# num_out=list(map(lambda n:n+1 if n>5 else n-1,lst))
# print(num_out)



#==============  filter ===============


# lst=[10,2,30,4]
#
# # print numbers greater than 10
# gt_ten=list(filter(lambda n:n>10,lst))
# print(gt_ten)
#
# # print even numbers from lst
#
# even=list(filter(lambda n:n%2==0,lst))
# print(even)



#===============  reduce ================

lst=[10,2,30,4]
sum=reduce(lambda n1,n2:n1+n2,lst)
print(sum)

product=reduce(lambda n1,n2:n1*n2,lst)
print(product)

max_num=reduce(lambda n1,n2:n1 if n1>n2 else n2,lst)
print(max_num)

min_num=reduce(lambda n1,n2:n1 if n1<n2 else n2,lst)
print(min_num)