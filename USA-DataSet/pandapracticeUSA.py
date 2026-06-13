import pandas as pd

df = pd.read_csv('RealEstate-USA.csv',delimiter=",",parse_dates=[11], date_format={'date_added': '%d-%m-%Y'})

print(df)
print(df.dtypes)
print('df.info():  ', df.info())

second_row = df.loc[1]
print(second_row)

second_row2 = df.loc[[1,3]]
print(second_row2)

second_row3 = df.loc[1:5]
print(second_row3)

second_row4 = df.loc[df['price'] < 100000]
print(second_row4)

second_row5 = df.loc[1:, 'price']
print(second_row5)

second_row6 = df.loc[:5,['price' , 'street']]
print(second_row6)

second_row7 = df.loc[:5, 'price' : 'street']
print(second_row7)

second_row8 = df.loc[df['city'] == 'ponce', 'price' : 'street']
print(second_row8)

#iloc testing

first_row = df.iloc[0]
print(first_row)

first_row1 = df.iloc[[1,4,6]]
print(first_row1)

first_row2 = df.iloc[2:5]
print(first_row2)

 
