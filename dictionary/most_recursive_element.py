# print most recursive element

pattern="ABACCDA"

a={}

word_count={"a":2,"b":5,"c":2,"d":4,"e":2}
wc_list=word_count.items()
# print(sorted(wc_list,key=lambda item:item[1],reverse=True))


#max

# print(max(wc_list,key=lambda item : item[1]))              (This is to find maximum recursive element )

#    OR

# print(max(word_count.items(),key=lambda i:i[1]))


# min

# print(min(word_count.items(),key=lambda i:i[1]))





# word_count={"a":2,"b":5,"c":2,"d":4,"e":2}
#
# for k,v in word_count.items():
#     print(max((k,v)))
#
#
#

# print(dir(dict))


# word_count="ABCDAABCD"
# # print(dir(set))
#
# m=word_count.split(" ")
# # s=set()
# # s.add(word_count)
# # print(s)
#
# print(m)




# word_count = {"a": 2, "b": 5, "c": 2, "d": 4, "e": 2}
# w=word_count.items()
# print(sorted(w,key=lambda p:p[1],reverse=True))

