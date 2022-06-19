# second recursive element

pattern="ABACCDA"
rec_char=[]
char_count={}
for char in pattern:
    if char in char_count:
        rec_char.append(char)
    else:
        char_count[char]=1
print(rec_char)
print("Second recursive element is",rec_char[1])





