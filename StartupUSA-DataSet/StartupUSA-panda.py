#startup_growth_investment_data.csv
import pandas as pd
import numpy as np

df = pd.read_csv('StartupUSA-DataSet/startup_growth_investment_data.csv', delimiter=",")
print(df.info())

print(df.head(3))
print(df.tail(3))

industry = df['Industry']
print(industry)

second_row4 = df.loc[df['Industry'] == 'HealthTech']
print(second_row4)

print("# Case 2 : using .loc with index_col")
df_index_col = pd.read_csv('StartupUSA-DataSet/startup_growth_investment_data.csv', delimiter=",", index_col='Startup Name')
print(df_index_col.iloc[0:5, 1:4])

df.drop(1, axis=0, inplace=True)
df.drop(columns='Country', inplace=True)

selected_rows = df.query('`Funding Rounds` > 5 or `Investment Amount (USD)` > 1000000')
print(selected_rows)

sorted_df = df.sort_values(by='Investment Amount (USD)')
print(sorted_df)

grouped = df.groupby('Industry')['Investment Amount (USD)'].sum()
print(grouped)