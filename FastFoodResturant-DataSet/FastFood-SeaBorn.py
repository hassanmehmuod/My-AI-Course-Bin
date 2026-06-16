import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

data = pd.DataFrame({'x': np.arange(100), 'y': np.random.rand(100).cumsum()})

sns.set_theme(style='darkgrid')
sns.lineplot(x='x', y='y', data=data)
plt.show()

sns.set_theme(style='whitegrid')
sns.lineplot(x='x', y='y', data=data)
plt.show()

sns.set_theme(style='darkgrid', rc={'axes.facecolor': 'grey', 'grid.color': 'white'})
sns.lineplot(x='x', y='y', data=data)
plt.show()

# FIX: Added the missing folder directory path prefix here
df = pd.read_csv('FastFoodResturant-DataSet/FastFoodRestaurants.csv', delimiter=",")
dffilter = df.head(40)

sns.set(style="whitegrid")

g = sns.displot(data=dffilter, x="city", y="latitude", hue="province", kind='hist')
g.figure.suptitle("FastFood Displot Hist")
g.figure.show()
read = input("Wait for me....")

# FIX: Shifted the categorical text variable 'city' out of the y-axis and into 'hue' to prevent the 2D KDE TypeError crash
g = sns.displot(data=dffilter, x="latitude", hue="city", kind='kde', fill=True)
g.figure.suptitle("FastFood Displot KDE")
g.figure.show()
read = input("Wait for me....")

g = sns.kdeplot(data=dffilter, x="latitude")
g.figure.suptitle("FastFood KDE plot")
g.figure.show()
read = input("Wait for me....")

g = sns.histplot(data=dffilter, x='city', y='latitude', hue='city', multiple="stack")
g.figure.suptitle("FastFood Histplot")
g.figure.show()
read = input("Wait for me....")

g = sns.scatterplot(x='city', y='latitude', data=dffilter)
g.figure.suptitle("FastFood Scatter")
g.figure.show()
read = input("Wait for me....")

g = sns.lineplot(data=dffilter, x="city", y="latitude")
g.figure.suptitle("FastFood Line")
g.figure.show()
read = input("Wait for me....")

g = sns.barplot(data=dffilter, x="city", y="latitude", legend=False)
g.figure.suptitle("FastFood Bar")
g.figure.show()
read = input("Wait for me....")

g = sns.catplot(data=dffilter, x="city", y="latitude")
g.figure.suptitle("FastFood Catplot")
g.figure.show()
read = input("Wait for me....")

glue = dffilter.pivot(columns="city", values="latitude")
g = sns.heatmap(glue)
g.figure.suptitle("FastFood Heatmap")
g.figure.show()
read = input("Wait for me....")