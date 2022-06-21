# # l = []
#
# # for i in range(1, 101):
# #     if i % 3 == 0 and i % 5 == 0:
# #         l.append(i)
# # print(l)
#
# # word count
#
# words="first second first second third fourth third fourth"
# wor=words.split(" ")
# wo={}
#
# for w in wor:
#     if w in wo:
#         wo[w]+=1
#     else:
#         wo[w]=1
# print(wo)
#
#
# # n1=5
# # n2=15
# # for i in range(n1,n2+1):
# #     if i>1:
# #         for j in range(2,i):
# #             if i%j==0:
# #                 break
# #         else:
# #            print(i)
#
#
# text="ok then ok then hi hello hi"
# # words=text.split(" ")
# # word_count={}
# # for w in words:
# #     if w in word_count:
# #         word_count[w]+=1
# #     else:
# #         word_count[w]=1
# # print(word_count)
#
#
# words = text.split(" ")
# word_count = {}
# for w in words:
#     if w in word_count:
#         word_count[w] += 1
#     else:
#         word_count[w] = 1
# print(word_count)
#
#
#


# d={"a":2,"b":4,"c":5}
# l=d.items()
# print(sorted(l,key=lambda p:p[1]))

print(dir(dict))