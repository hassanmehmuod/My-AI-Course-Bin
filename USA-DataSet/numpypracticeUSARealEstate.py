import numpy as np



brokeredby , status , price , bed , bath= np.genfromtxt('RealEstate-USA.csv', delimiter= ',', usecols = (0,1,2,3,4), unpack=True, dtype=None,skip_header=1)
print(brokeredby)
print(status)
print(price)
print(bed)
print(bath)


print("Real estate mean;  ", np.mean(price))
print("Real estate average;  ", np.average(price))
print("Real estate percentile;  ", np.percentile(price, 25))
print("Real estate percentile:  ",np.percentile(price, 75))
print("Real estate min:  ",np.min(price))
print("Real estate max:  ",np.max(price))

print("Real estate Price square: " , np.square(price))
print("Real estate Price sqrt: " , np.sqrt(price))
print("Real estate Price pow: " , np.power(price,price))
print("Real estate Price abs: " , np.abs(price))