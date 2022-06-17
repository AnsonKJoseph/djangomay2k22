# lst = [
#     [10, 11],
#     [13, 45],
#     [50, 15],
#     [60, 16]
# ]
#
# flatten_list=[num for sub_lst in lst for num in sub_lst ]
# print(flatten_list)




# print numbers in the list greater than 16

# lst = [
#     [10, 11],
#     [13, 45],
#     [50, 15],
#     [60, 16]
# ]
# flatten_list=[num for sub_lst in lst for num in sub_lst ]
# nums_greater_16=[num for num in flatten_list if num>16]
# print(nums_greater_16)




# print odd numbers from flatten_list

# lst = [
#     [10, 11],
#     [13, 45],
#     [50, 15],
#     [60, 16]
# ]
# flatten_list=[num for sub_list in lst for num in sub_list]
# odd_numbers=[num for num in flatten_list if num%2!=0]
# print(odd_numbers)
#
#

# print sum of even numbers

lst = [
    [10, 11],
    [13, 45],
    [50, 15],
    [60, 16]
]

flatten_lst=[num for sub_lst in lst for num in sub_lst]
even_nums=[num for num in flatten_lst if num%2==0]
print(sum(even_nums))
