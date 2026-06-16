#Real_Estate_Sales_2001-2022_GL-Short.csv
import numpy as np

# Column 0 = Serial Number, Column 5 = Assessed Value, Column 6 = Sale Amount
# FIX: Added invalid_raise=False to drop rows with extra text commas safely without crashing
ids, price, long, lat = np.genfromtxt('RealEstate-Sales/Real_Estate_Sales_2001-2022_GL-Short.csv', delimiter=',', usecols=(0,6,5,5), unpack=True, dtype=float, skip_header=1, invalid_raise=False)

print("Real Estate Sales Price mean: " , np.mean(price))
print("Real Estate Sales Price std: " , np.std(price))
print("Real Estate Sales Price min : " , np.min(price))
print("Real Estate Sales Price max : " , np.max(price))

print("Real Estate Sales Price square: " , np.square(price))
print("Real Estate Sales Price sqrt: " , np.sqrt(price))

addition = long + lat
subtraction = long - lat
print("Addition:", addition)

pricePie = (price/np.pi) + 1
print("Sine values:", np.sin(pricePie))
print("Natural logarithm values:", np.log(pricePie))

D2LongLat = np.array([long[:70], lat[:70]])
print("Shape:", D2LongLat.shape)

D2LongLatSlice = D2LongLat[0:1:1 , 1:5:1]
print("Splicing array: " , D2LongLatSlice)

for elem in np.nditer(D2LongLat):
    print(elem)

for index, elem in np.ndenumerate(D2LongLat):
    print(index, elem)

D2LongLat1TO298 = np.reshape(D2LongLat, (1, 140))
print("Reshaped shape: ", D2LongLat1TO298.shape)