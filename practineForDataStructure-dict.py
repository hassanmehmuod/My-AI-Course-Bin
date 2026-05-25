MobileDict = {
    'mobile' : 'Iphone 13 pro max',
    'price'  : 178000,
    'weight' : 167.5    
}

print(type(MobileDict))
print(MobileDict)

for i in MobileDict:
    print(i)

MobileDict.pop('weight')
print(MobileDict)

for i in MobileDict:
    print(MobileDict[i])

MobileDict['title'] = 'iphone'
print(MobileDict)

MobileDict['price'] = 189000
print(MobileDict)

for i in MobileDict:
    print(MobileDict[i])