f = open("abc.txt","w")
# for line in f:
#     print(line)

# lines= list(f)
# print(lines)
#
# out = [line.rstrip("\n") for line in f]
# print(out)

lst=["python","javascript","c"]

company_name="luminar"
for lan in lst:
    lan+="\n"
    f.write(lan)