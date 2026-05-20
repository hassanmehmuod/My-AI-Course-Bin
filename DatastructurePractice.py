#Set

ProductMobileSet = ("Iphone", 34.21, 12, "Red")
print(ProductMobileSet)
print(type(ProductMobileSet))
for x in ProductMobileSet:
    print(x)



#Dictionary

ProductMobileDictionary = {
    'title': 'iphone',
    'Price': 34.50,
    'colour': 'red'
}
print("Mobile name is ", ProductMobileDictionary['title'])
print(ProductMobileDictionary)
print(type(ProductMobileDictionary))
for x in ProductMobileDictionary:
    print(x)

for x in ProductMobileDictionary:
    print(ProductMobileDictionary[x])



#List
Productmobilelist = ['Iphone', 34.50, 12, 'Red']
print(Productmobilelist)
print(type(Productmobilelist))
print(Productmobilelist[1])
for x in ProductMobileSet:
    print(x)


#Tuple
Productmobiletuple = ('Iphone', 34.50, 12, 'Red')
print(Productmobiletuple)
print(type(Productmobiletuple))
print(Productmobiletuple[2])
for x in Productmobiletuple:
    print(x)