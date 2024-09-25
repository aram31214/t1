n=input("enter your name")

print("name"+n)

names=["aram","ahmad","ali"]
print(names[0])

names.append("hossam")
print(names)
names.sort()
print(names)

aramoset=set()
aramoset.add("aram")
aramoset.add("ahmad")
aramoset.add("ali")
aramoset.remove("ali")

print(aramoset)
print(f"the length {len(aramoset)}")
print(len(aramoset))


house={"aram":"1","ahmad":"2","ali":"3"}

print(house)
print(house["aram"])
house["ahmad"]="4"

print(house)
house["amora"]="1"

print(house)