master_word = "aabbbccaadtdteeggm"
chk_word = "bbaadtev"

mw_dic = {}
flag = 0

# mc_count = {}

for char in master_word:
    if char in mw_dic:  #
        mw_dic[char] += 1
    else:
        mw_dic[char] = 1
print(mw_dic)

# {'a': 4, 'b': 2, 'c': 2, 'd': 2, 't': 2, 'e': 2, 'g': 1, 'm': 1}
for char in chk_word:
    if char in mw_dic:  # a
        cur_count = mw_dic[char]
        if cur_count > 0:
            mw_dic[char] -= 1
        # elif cur_count == 0:
        #     flag = 1

    else:
        flag = 1

print(True if flag == 0 else False)




#    my own program


# master word="abbcceddffggt"
# check_word = "egg"


# mw = "abbcceddffggt"
# chk_word = " "
# dupl = " "
# for i in mw:
#     if i not in chk_word:
#         pass
#     else:
#         dupl = dupl + i
# # print(dupl)
# if chk_word == dupl:
#     print(True)
# else:
#     print(False)
