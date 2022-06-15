# #         lambda function
#
# def sub_nums(n1,n2):
#     return n1-n2
# print(sub_nums(10,5))
#
# #       instead
#
# sub=lambda n1,n2:n1-n2
# print(sub(10,5))
#
# #find cube of a number
#
#
# cube=lambda n:n**3
# print(cube(2))
#
#
#
#
#
# def max_two(n1,n2):
#     return n1 if n1>n2 else n2
# print(max_two(2,3))
#
#
#
#
# max_two=lambda n1,n2:n1 if n1>n2 else n2
# print(max_two(2,3))
#
#
#
#
# smart_sub=lambda n1,n2:n1-n2 if n1>n2 else n2-n1
# print(smart_sub(1,3))
#
#
# # find sum of numbers in range


#
# def range_sum(n1,n2):
#     return sum(range(n1,n2))
# print(range_sum(1,5))


# using lambda

range_sum=lambda n1,n2:sum(range(n1,n2))
print(range_sum(1,5))