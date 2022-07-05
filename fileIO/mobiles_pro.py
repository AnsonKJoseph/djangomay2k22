fread=open("mobiles.txt","r")
all_mobiles=[mobiles.rstrip("\n").split(",") for mobiles in fread ]

#                     OR

# for line in fread:
#     mobile=line.rstrip("\n").split(",")
#     all_mobiles.append(mobile)
print(all_mobiles)

# print costly mobile
costly_mobile=max(all_mobiles,key=lambda mob:int(mob[2]))
print(costly_mobile)


# print all 5g mobiles

five_g=[mob for mob in all_mobiles if mob[3]=="5g"]
print(five_g)


