#FastFoodRestaurants.csv
import numpy as np

# Column 4 = latitude, Column 5 = longitude
# FIX: Added invalid_raise=False to drop corrupt rows, and changed usecols to separate indices (4, 4, 5, 4) to align with your variable variables properly
ids, price, long, lat = np.genfromtxt(
    'FastFoodResturant-DataSet/FastFoodRestaurants.csv', 
    delimiter=',', 
    usecols=(4, 4, 5, 4), 
    unpack=True, 
    dtype=float, 
    skip_header=1,
    invalid_raise=False
)

print(ids)
print(price)
print(long)
print(lat)

print(np.min(price))

# FastFoodRestaurants price - statistics operations
print("FastFoodRestaurants Price mean: " , np.mean(price))
print("FastFoodRestaurants Price average: " , np.average(price))
print("FastFoodRestaurants Price std: " , np.std(price))
print("FastFoodRestaurants Price mod: " , np.median(price))
print("FastFoodRestaurants Price percentile - 25: " , np.percentile(price,25))
print("FastFoodRestaurants Price percentile  - 75: " , np.percentile(price,75))
print("FastFoodRestaurants Price percentile  - 3: " , np.percentile(price,3))
print("FastFoodRestaurants Price min : " , np.min(price))
print("FastFoodRestaurants Price max : " , np.max(price))

# FastFoodRestaurants price - maths operations
print("FastFoodRestaurants Price square: " , np.square(price))
print("FastFoodRestaurants Price sqrt: " , np.sqrt(price))
print("FastFoodRestaurants Price pow: " , np.power(price,price))
print("FastFoodRestaurants Price abs: " , np.abs(price))

# Perform basic arithmetic operations
addition = long + lat
subtraction = long - lat
multiplication = long * lat
division = long / lat

print(" FastFoodRestaurants Long - lat - Addition:", addition)
print(" FastFoodRestaurants Long - lat - Subtraction:", subtraction)
print(" FastFoodRestaurants Long - lat - Multiplication:", multiplication)
print(" FastFoodRestaurants Long - lat - Division:", division)

#Trigonometric Functions
pricePie = (price/np.pi) +1
sine_values = np.sin(pricePie)
cosine_values = np.cos(pricePie)
tangent_values = np.tan(pricePie)

print("FastFoodRestaurants Price - div - pie - Sine values:", sine_values)
print("FastFoodRestaurants Price - div - pie Cosine values:", cosine_values)
print("FastFoodRestaurants Price - div - pie Tangent values:", tangent_values)
print("FastFoodRestaurants Price - div - pie - Exponential values:", np.exp(pricePie))

log_array = np.log(np.abs(pricePie))
log10_array = np.log10(np.abs(pricePie))

print("FastFoodRestaurants Price - div - pie - Natural logarithm values:", log_array)
print("FastFoodRestaurants Price - div - pie = Base-10 logarithm values:", log10_array)

sinh_values = np.sinh(pricePie)
print("FastFoodRestaurants Price - div - pie - Hyperbolic Sine values:", sinh_values)

cosh_values = np.cosh(pricePie)
print("FastFoodRestaurants Price - div - pie - Hyperbolic Cosine values:", cosh_values)

tanh_values = np.tanh(pricePie)
print("FastFoodRestaurants Price - div - pie -Hyperbolic Tangent values:", tanh_values)

asinh_values = np.arcsinh(pricePie)
print("FastFoodRestaurants Price - div - pie -Inverse Hyperbolic Sine values:", asinh_values)

acosh_values = np.arccosh(np.abs(pricePie) + 1)
print("FastFoodRestaurants Price - div - pie -Inverse Hyperbolic Cosine values:", acosh_values)

D2LongLat = np.array([long[:200], lat[:200]])

print ("FastFoodRestaurants Long Plus Lat - 2 dimentional arrary - " ,D2LongLat)
print("FastFoodRestaurants Long Plus Lat - 2 dimentional arrary - dimension" , D2LongLat.ndim) 
print("FastFoodRestaurants Long Plus Lat - 2 dimentional arrary - total number of elements" ,D2LongLat.size)
print("FastFoodRestaurants Long Plus Lat - 2 dimentional arrary - gives size of array in each dimension" ,D2LongLat.shape)
print("FastFoodRestaurants Long Plus Lat - 2 dimentional arrary - data type" ,D2LongLat.dtype) 

D2LongLatSlice = D2LongLat[0:1:1 , 1:5:1]
print("FastFoodRestaurants Long Plus Lat - 2 dimentional arrary - Splicing array - D2LongLat[:1Scope] " , D2LongLatSlice)
D2LongLatSlice2 = D2LongLat[:1, 4:15:4]
print("FastFoodRestaurants Long Plus Lat - 2 dimentional arrary - Splicing array - D2LongLat[:1, 4:15:4] " , D2LongLatSlice2)

D2LongLatSliceItemOnly = D2LongLatSlice[0,1]
print("FastFoodRestaurants Long Plus Lat - 2 dimentional arrary - Index array - D2LongLatSlice[1,5] " , D2LongLatSliceItemOnly)
D2LongLatSlice2ItemOnly = D2LongLatSlice2[0, 2]
print("FastFoodRestaurants Long Plus Lat - 2 dimentional arrary - index array - D2LongLatSlice2[0, 2] " , D2LongLatSlice2ItemOnly)

for elem in np.nditer(D2LongLat):
    print(elem)

for index, elem in np.ndenumerate(D2LongLat):
    print(index, elem)

D2LongLat1TO298 = np.reshape(D2LongLat, (1, 400))
print("FastFoodRestaurants Long Plus Lat - 2 dimentional arrary - np.reshape: " , D2LongLat1TO298)