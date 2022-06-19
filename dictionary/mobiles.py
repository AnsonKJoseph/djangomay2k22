mobiles={
    "mobile_name":"redminote12pro",
    "display":"led",
    "price":45000,
    "ram":"6gb",
    "memory":"64gb"
}

# print(mobiles["mobile_name"])
#
# print("display" in mobiles)

# mobiles["price"]=50000
# print(mobiles)
#

# mobiles["price"]+=1000
# print(mobiles)

# get()  method

# print(mobiles.get("mobile_name"))

# print(mobiles.get("ram"))

# if "band" in mobiles:
#     mobiles["band"]="5g"
# else:
#     mobiles["band"]="4g"
# print(mobiles)

#         OR

mobiles["band"]="5g" if "band" in mobiles else "4g"
print(mobiles)


# mobile price update cur_price-1000 if cur_price>40000 else cur_price-500
#
# if mobiles["price"]>40000:
#     mobiles["price"]+=-1000
# else:
#     mobiles["price"]+=500
# print(mobiles)

#         OR

mobiles["price"]=mobiles["price"]-1000 if mobiles["price"]>40000 else mobiles["price"]-500
print(mobiles)






