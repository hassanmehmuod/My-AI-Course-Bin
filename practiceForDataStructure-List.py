MobileList = ["iphone 13 pro max", 189000, 12.5, "Iphone", True]
print(type(MobileList))
print(MobileList)

for i in MobileList:
    print(i)

MobileList.append("Dubai")
print(MobileList)

MobileList.insert(2, 135.5)
print(type(MobileList[2]))

MobileList.remove(189000)
print(MobileList)

MobileList.pop(4)
print(MobileList)