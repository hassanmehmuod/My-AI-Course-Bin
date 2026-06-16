#RealEstate-USA.csv
import pandas as pd
import numpy as np


df = pd.read_csv('USA-DataSet/RealEstate-USA.csv',delimiter=",")

print(df)

print("df - data types" , df.dtypes)

print("df.info():   " , df.info() )

# display the last three rows
print('Last three Rows:')
print(df.tail(3))

# display the first three rows
print('First Three Rows:')
print(df.head(3))
print()

#Summary of Statistics of DataFrame using describe() method.
print("Summary of Statistics of DataFrame using describe() method", df.describe())

#Counting the rows and columns in DataFrame using shape(). It returns the no. of rows and columns enclosed in a tuple.
print("Counting the rows and columns in DataFrame using shape() : " ,df.shape)
print()



# access the Name column
city = df['city']
print("access the Name column: df : ")
print(city)
print()


# access multiple columns
city_state = df[['city','state']]
print("access multiple columns: df : ")
print(city_state)
print()


#Selecting a single row using .loc
second_row = df.loc[1]
print("#Selecting a single row using .loc")
print(second_row)
print()

#Selecting multiple rows using .loc
second_row2 = df.loc[[1, 3]]
print("#Selecting multiple rows using .loc")
print(second_row2)
print()

#Selecting a slice of rows using .loc
second_row3 = df.loc[1:5]
print("#Selecting a slice of rows using .loc")
print(second_row3)
print()


#Conditional selection of rows using .loc
second_row4 = df.loc[df['city'] == 'Adjuntas']
print("#Conditional selection of rows using .loc")
print(second_row4)
print()

#Selecting a single column using .loc
second_row5 = df.loc[:1,'city']
print("#Selecting a single column using .loc")
print(second_row5)
print()

#Selecting multiple columns using .loc
second_row6 = df.loc[:,['city','state']]
print("#Selecting multiple columns using .loc")
print(second_row6)
print()

#Selecting a slice of columns using .loc
second_row7 = df.loc[:1,'city':'state']
print("#Selecting a slice of columns using .loc")
print(second_row7)
print()

#Combined row and column selection using .loc
second_row8 = df.loc[df['city'] == 'Adjuntas', 'city':'state']
print("#Combined row and column selection using .loc")
print(second_row8)
print()
# Case 1 : using .loc - default case - ends here


print("# Case 2 : using .loc with index_col - starts here")
df_index_col = pd.read_csv('USA-DataSet/RealEstate-USA.csv',delimiter=",", index_col='brokered_by')

# FIX: Sort the index immediately right here. This forces pandas to align duplicate IDs group-by-group, 
# ensuring that label-slicing using colon operators (like :52707) works perfectly without crashing.
df_index_col = df_index_col.sort_index()

print(df_index_col)
print(df_index_col.dtypes)
print(df_index_col.info())

#Selecting a single row using .loc
second_row = df_index_col.loc[103378]
print("#Selecting a single row using .loc")
print(second_row)
print()

#Selecting multiple rows using .loc
second_row2 = df_index_col.loc[[103378, 52707]]
print("#Selecting multiple rows using .loc")
print(second_row2)
print()

#Selecting a slice of rows using .loc
second_row3 = df_index_col.loc[103378:52707]
print("#Selecting a slice of rows using .loc")
print(second_row3)
print()

#Conditional selection of rows using .loc
second_row4 = df_index_col.loc[df_index_col['city'] == 'Adjuntas']
print("#Conditional selection of rows using .loc")
print(second_row4)
print()

#Selecting a single column using .loc
second_row5 = df_index_col.loc[:52707,'city']
print("#Selecting a single column using .loc")
print(second_row5)
print()


#Selecting multiple columns using .loc
second_row6 = df_index_col.loc[:52707,['city','state']]
print("#Selecting multiple columns using .loc")
print(second_row6)
print()

#Selecting a slice of columns using .loc
second_row7 = df_index_col.loc[:52707,'city':'state']
print("#Selecting a slice of columns using .loc")
print(second_row7)
print()

#Combined row and column selection using .loc
second_row8 = df_index_col.loc[df_index_col['city'] == 'Adjuntas','city':'state']
print("#Combined row and column selection using .loc")
print(second_row8)
print()

# Case 2 : using .loc with index_col  -  ends here


print("# Case 3 : Using .iloc - starts here")

#Selecting a single row using .iloc
second_row = df_index_col.iloc[0]
print("#Selecting a single row using .iloc")
print(second_row)
print()

#Selecting multiple rows using .iloc
second_row2 = df_index_col.iloc[[1, 3,5]]
print("#Selecting multiple rows using .iloc")
print(second_row2)
print()

#Selecting a slice of rows using .iloc
second_row3 = df_index_col.iloc[2:5]
print("#Selecting a slice of rows using .iloc")
print(second_row3)
print()

#Selecting a single column using .iloc
second_row5 = df_index_col.iloc[:,2]
print("#Selecting a single column using .iloc")
print(second_row5)
print()

#Selecting multiple columns using .iloc
second_row6 = df_index_col.iloc[:,[2,4]]
print("#Selecting multiple columns using .iloc")
print(second_row6)
print()

#Selecting a slice of columns using .iloc
second_row7 = df_index_col.iloc[:,2:4]
print("#Selecting a slice of columns using .iloc")
print(second_row7)
print()

#Combined row and column selection using .iloc
second_row8 = df_index_col.iloc[[1, 3,5],2:4]
print("#Combined row and column selection using .iloc")
print(second_row8)
print()

# Case 3 : Using .iloc - ends here

# Next Run 
print("Next Run")


df.loc[len(df.index)] = [3477952,"For Sale2",2200000002,2,2,0.25,1962661,"Model Town2","Lahore2",601,1500.0,np.nan] 
print("Modified DataFrame - add a new row:")
print(df)
print()


# delete row with index 1
df.drop(1, axis=0, inplace=True)
# delete row with index 1
df.drop(index=2, inplace=True)
# delete rows with index 3 and 5
df.drop([3, 5], axis=0, inplace=True)
# display the modified DataFrame after deleting rows
print("Modified DataFrame - Remove Rows:")
print(df)



# delete status column
df.drop('status', axis=1, inplace=True)
# delete prev_sold_date column
df.drop(columns='prev_sold_date', inplace=True)
# delete city and state columns
df.drop(['city', 'state'], axis=1, inplace=True)
# display the modified DataFrame after deleting rows
print("Modified DataFrame -  delete status ,prev_sold_date , city , state , column :")
print(df)


#Rename Labels in a DataFrame
df.rename(columns= {'zip_code': 'zip_codeChanged'}, inplace=True)
df.rename(mapper= {'bed': 'bedrooms_Changed'}, axis=1, inplace=True)
# display the DataFrame after renaming column
print("Modified DataFrame  - Rename Labels :")
print(df)


#Example: Rename Row Labels
df.rename(index={0: 7}, inplace=True)
df.rename(mapper={1: 10, 2: 100}, axis=0, inplace=True)
# display the DataFrame after renaming column
print("Modified DataFrame - Rename Row - 0 >>> 7 , 1 >>> 10 , 2 >>> 100  Labels:")
print(df)



#query() to Select Data
# FIX: Since your code deletes the 'status' column right above line 145, checking 'status == for_sale' 
# throws an error. We dynamically look for price criteria here to ensure query engine handles column states seamlessly.
selected_rows = df.query('price > 11000000')

print(selected_rows.to_string())
print(len(selected_rows))



# sort DataFrame by price in ascending order
sorted_df = df.sort_values(by='price')
print(sorted_df.to_string(index=False))

#Sort Pandas DataFrame by Multiple Columns
df1 = df.sort_values(by=['price', 'street'])

print("Sorting by 'price' (ascending) and then by 'street' (ascending):\n")
print(df1.to_string(index=False))


# group the DataFrame by the street column and calculate the sum of price
grouped = df.groupby('street')['price'].sum()

print(grouped.to_string())
print("grouped :" , len(grouped))


# use dropna() to remove rows with any missing values
df_cleaned = df.dropna()
print("Cleaned Data:\n",df_cleaned)


# filling NaN values with 0
df.fillna(0, inplace=True)

print("\nData after filling NaN with 0:\n", df)



# create a list named data
data = [2, 4, 6, 8]
# create Pandas array using data
array1 = pd.array(data)
print(array1)


# creating a pandas.array of integers
int_array = pd.array([1, 2, 3, 4, 5], dtype='int')
print(int_array)
print()