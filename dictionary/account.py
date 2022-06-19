account={
    "acc_no":1234,
    "type":"savings",
    "pname":"ram",
    "branch":"ptm"
}

# print(account["acc_no"])
#
# print("balance" in account)
#
# account["balance"]=5000
# print(account)
#
#
# account["balance"]+=1000
# print(account)

# get()  method

# print(account.get("acc_no"))
#
# print(account.get("pname"))

if "branch" in account:
    account["branch"]="ktm"
else:
    account["branch"]="ekm"
print(account)






