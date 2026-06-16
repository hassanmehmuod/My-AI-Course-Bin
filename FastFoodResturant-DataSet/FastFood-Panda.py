#FastFoodRestaurants.csv
import pandas as pd
import numpy as np

df = pd.read_csv('FastFoodResturant-DataSet/FastFoodRestaurants.csv', delimiter=",")
print(df)
print("df - data types" , df.dtypes)
print("df.info(): ", df.info())

print('Last three Rows:')
print(df.tail(3))
print('First Three Rows:')
print(df.head(3))

print("Summary of Statistics:", df.describe())
print("Counting rows and columns via shape: " ,df.shape)

city = df['city']
print(city)

city_province = df[['city','province']]
print(city_province)

second_row = df.loc[1]
print(second_row)

second_row2 = df.loc[[1, 3]]
print(second_row2)

second_row3 = df.loc[1:5]
print(second_row3)

second_row4 = df.loc[df['city'] == 'Massena']
print(second_row4)

second_row5 = df.loc[:1,'city']
print(second_row5)

second_row6 = df.loc[:,['city','province']]
print(second_row6)

second_row7 = df.loc[:1,'city':'province']
print(second_row7)

second_row8 = df.loc[df['city'] == 'Massena', 'city':'province']
print(second_row8)

print("# Case 2 : using .loc with index_col")
# FIX: Fixed file directory path to include 'FastFoodResturant-DataSet/' and added .sort_index() to keep positional index slicing operational
df_index_col = pd.read_csv('FastFoodResturant-DataSet/FastFoodRestaurants.csv', delimiter=",", index_col='postalCode')
df_index_col = df_index_col.sort_index()

print(df_index_col)
second_row = df_index_col.loc['43160']
print(second_row)

print("# Case 3 : Using .iloc")
second_row = df_index_col.iloc[0]
print(second_row)

second_row2 = df_index_col.iloc[[1, 3,5]]
print(second_row2)

second_row3 = df_index_col.iloc[2:5]
print(second_row3)

second_row5 = df_index_col.iloc[:,2]
print(second_row5)

second_row6 = df_index_col.iloc[:,[2,4]]
print(second_row6)

second_row7 = df_index_col.iloc[:,2:4]
print(second_row7)

second_row8 = df_index_col.iloc[[1, 3,5],2:4]
print(second_row8)

df.loc[len(df.index)] = ["Test Address","Lahore","PK","keys123",31.5,74.3,"New Fast Food","54000","Punjab","http://test.com"] 
print(df)

df.drop(1, axis=0, inplace=True)
df.drop(columns='websites', inplace=True)

df.rename(columns= {'province': 'provinceChanged'}, inplace=True)
print(df)

selected_rows = df.query('city == \'Massena\' or latitude > 40')
print(selected_rows)

sorted_df = df.sort_values(by='latitude')
print(sorted_df)

grouped = df.groupby('city')['latitude'].sum()
print(grouped)

df_cleaned = df.dropna()
df.fillna(0, inplace=True)

data = [2, 4, 6, 8]
array1 = pd.array(data)
print(array1)