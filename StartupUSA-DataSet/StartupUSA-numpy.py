#startup_growth_investment_data.csv
import numpy as np

# Column 2 = Funding Rounds, Column 3 = Investment Amount, Column 5 = Number of Investors
ids, price, long, lat = np.genfromtxt('StartupUSA-DataSet/startup_growth_investment_data.csv', delimiter=',', usecols=(2,3,2,5), unpack=True, dtype=float, skip_header=1)

print("Startup Price mean: " , np.mean(price))
print("Startup Price std: " , np.std(price))
print("Startup Price min : " , np.min(price))
print("Startup Price max : " , np.max(price))

print("Startup Price square: " , np.square(price))
print("Startup Price sqrt: " , np.sqrt(price))

addition = long + lat
subtraction = long - lat
print("Addition:", addition)

pricePie = (price/np.pi) + 1
print("Sine values:", np.sin(pricePie))
print("Natural logarithm values:", np.log(pricePie))

D2LongLat = np.array([long[:200], lat[:200]])
print("Shape:", D2LongLat.shape)

D2LongLatSlice = D2LongLat[0:1:1 , 1:5:1]
print("Splicing array: " , D2LongLatSlice)

for elem in np.nditer(D2LongLat):
    print(elem)

for index, elem in np.ndenumerate(D2LongLat):
    print(index, elem)

D2LongLat1TO298 = np.reshape(D2LongLat, (1, 400))
print("Reshaped shape: ", D2LongLat1TO298.shape)