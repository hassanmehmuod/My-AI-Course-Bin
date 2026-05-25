MobileSet = {"iphone 13 pro max", 189000, 12.5, "Iphone", True}
print(type(MobileSet))
print(MobileSet)

for i in MobileSet:
    print(i)

MobileSet.add(34.5)
print(MobileSet)

MobileSet.discard(34.5)
print(MobileSet)