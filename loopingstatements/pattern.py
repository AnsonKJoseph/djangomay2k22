#    c1 c2 c3 c4
# r1  1  2  3  4
# r2  1  2  3  4
# r3  1  2  3  4

# for row in range(1, 4):  # 7th video (for reference)
#     for col in range(1, 5):
#         print(col, end=" ")
#     print()





# 1  1  1  1
# 2  2  2  2
# 3  3  3  3
# 4  4  4  4

# for row in range(1, 5):  # 7th video (for reference)
#     for col in range(1, 5):
#         print(row, end=" ")
#     print()




# 1
# 1  2
# 1  2  3
# 1  2  3  4
#
# for row in range(1,5):
#     for col in range(1,row+1):
#         print(col,end=" ")
#     print()




#
#  #
#  #  #
#  #  #  #


# for row in range(1,5):
#   for j in range(1,row+1):                      #7th video
#        print("#",end=" ")
#   print()
#



#  #  #  #
#  #  #
#  #
#

# for row in range(1,5):
#     for col in range(5,row,-1):                            #7th video
#         print("#",end=" ")
#     print()
#




# full pyramid

       #

      #  #

     #  #  #

    #  #  #  #

  #  #  #  #  #

 #  #  #  #  #  #



# for row in range(1,7):
#     str=""                                                      # 8th video
#     for space in range(1,(7-row)):
#         str+=" "
#     for _ in range(1,(row+1)):
#         str+="* "
#     print(str)









 # Hollow pyramid

       #

      #  #

     #     #

    #        #

  #           #

 #  #  #  #  #  #


