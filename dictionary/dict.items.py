dict={"k1":10,"k2":"hello","k3":True}
print(dict.get("k4"))

for k,v in dict.items():
    print(k,v)

for v in dict.values():
    print(v)
    
dict.pop("k3")
print(dict)
