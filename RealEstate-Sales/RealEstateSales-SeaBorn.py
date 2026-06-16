import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

data = pd.DataFrame({'x': np.arange(100), 'y': np.random.rand(100).cumsum()})

sns.set_theme(style='darkgrid')
sns.lineplot(x='x', y='y', data=data)
plt.show()

df = pd.read_csv('RealEstate-Sales/Real_Estate_Sales_2001-2022_GL-Short.csv', delimiter=",")
dffilter = df.head(40)

sns.set(style="whitegrid")

g = sns.displot(data=dffilter, x="Town", y="Sale Amount", hue="Property Type", kind='hist')
g.figure.suptitle("Real Estate Sales Displot Hist")
g.figure.show()
read = input("Wait for me....")

g = sns.scatterplot(x='Town', y='Sale Amount', data=dffilter)
g.figure.suptitle("Real Estate Sales Scatter")
g.figure.show()
read = input("Wait for me....")

g = sns.barplot(data=dffilter, x="Town", y="Sale Amount", legend=False)
g.figure.suptitle("Real Estate Sales Bar")
g.figure.show()
read = input("Wait for me....")