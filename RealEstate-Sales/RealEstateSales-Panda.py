#Real_Estate_Sales_2001-2022_GL-Short.csv
import pandas as pd
import numpy as np

df = pd.read_csv('RealEstate-Sales/Real_Estate_Sales_2001-2022_GL-Short.csv', delimiter=",")
print(df.info())

print(df.head(3))
print(df.tail(3))

towns = df['Town']
print(towns)

second_row4 = df.loc[df['Town'] == 'Ansonia']
print(second_row4)

print("# Case 2 : using .loc with index_col")
# FIX: Added the missing 'RealEstate-Sales/' folder directory path to prevent the FileNotFoundError crash
df_index_col = pd.read_csv('RealEstate-Sales/Real_Estate_Sales_2001-2022_GL-Short.csv', delimiter=",", index_col='Serial Number')
print(df_index_col.iloc[0:5, 1:4])

df.drop(1, axis=0, inplace=True)
df.drop(columns='Location', inplace=True)

selected_rows = df.query('`Sale Amount` > 200000 or `Assessed Value` > 100000')
print(selected_rows)

sorted_df = df.sort_values(by='Sale Amount')
print(sorted_df)

grouped = df.groupby('Town')['Sale Amount'].sum()
print(grouped)