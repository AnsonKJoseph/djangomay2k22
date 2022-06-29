# master word="abbcceddffggt"
# check_word = "egg"


mw = "abbcceddffggt"
chk_word = "cat"
dupl = ""
for i in mw:
    if i not in chk_word:
        pass
    else:
        dupl = dupl + i
# print(dupl)
if chk_word==dupl:
    print(True)
else:
    print(False)
