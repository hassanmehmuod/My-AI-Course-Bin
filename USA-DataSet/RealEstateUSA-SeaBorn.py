import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

# Sample data
data = pd.DataFrame({'x': np.arange(100), 'y': np.random.rand(100).cumsum()})

# Set the theme
sns.set_theme(style='darkgrid')

# Create a plot
sns.lineplot(x='x', y='y', data=data)
plt.show()

# Other themes can be set similarly
sns.set_theme(style='whitegrid')
sns.lineplot(x='x', y='y', data=data)
plt.show()

sns.set_theme(style='dark')
sns.lineplot(x='x', y='y', data=data)
plt.show()

sns.set_theme(style='white')
sns.lineplot(x='x', y='y', data=data)
plt.show()

sns.set_theme(style='ticks')
sns.lineplot(x='x', y='y', data=data)
plt.show()


# Customize the theme
sns.set_theme(style='darkgrid', rc={'axes.facecolor': 'grey', 'grid.color': 'white'})

# Create a plot
sns.lineplot(x='x', y='y', data=data)
plt.show()


# RealEstate-USA data - based examples
df = pd.read_csv('USA-DataSet/RealEstate-USA.csv',delimiter=",")

print(df.dtypes)
dffilter= df.head(40)
dffilter100= df.head(100)

sns.set(style="whitegrid")


#kind='hist'  
g=sns.displot(data=dffilter, x="city" , y="price" , hue="state",  kind='hist'  )
g.figure.suptitle("sns.displot(data=dffilter, x=city , y=price , hue=state,  kind='hist'  )"  )

# Display the plot
g.figure.show()
read = input("Wait for me....5")


# FIX: Changed from a 2D KDE plot to a 1D density distribution where 'city' is used as the 'hue' classification factor.
g=sns.displot(data=dffilter, x="price" , hue="city" , kind='kde', fill=True)
g.figure.suptitle("sns.displot(data=dffilter, x=price , hue=city , kind='kde' )"  )

# Display the plot
g.figure.show()
read = input("Wait for me....5")


#kind='kde'
g=sns.kdeplot(data=dffilter, x="price")
g.figure.suptitle("sns.kdeplot(data=dffilter, x=price)"  )

# Display the plot
g.figure.show()
read = input("Wait for me....5")


g = sns.histplot(data=dffilter, x='city', y='price', hue='city', multiple="stack")
g.figure.suptitle("sns.histplot(data=dffilter, x='city', y='price', hue='city', multiple=stack)"  )
# Display the plot
g.figure.show()
read = input("Wait for me....5")


# Use Seaborn to create a plot
g = sns.scatterplot(x='city', y='price', data=dffilter)
g.figure.suptitle("sns.scatterplot(x='city', y='price', data=dffilter)"  )
g.figure.show()
read = input("Wait for me....5")


g=sns.lineplot(data=dffilter, x="city" , y="price"  )
g.figure.suptitle("sns.lineplot(data=dffilter, x=city , y=price  )"  )
# Display the plot
g.figure.show()
read = input("Wait for me....5")



g=sns.barplot(data=dffilter, x="city", y="price", legend=False)
g.figure.suptitle("sns.barplot(data=dffilter, x=city, y=price, legend=False)"  )
# Display the plot
g.figure.show()
read = input("Wait for me....5")


g=sns.catplot(data=dffilter, x="city", y="price")
g.figure.suptitle("sns.catplot(data=df, x=city, y=price)"  )
# Display the plot
g.figure.show() 
read = input("Wait for me....5")



glue = dffilter.pivot(columns="city", values="price")

g=sns.heatmap(glue)
g.figure.suptitle("sns.heatmap(glue)  - glue = dffilter.pivot(columns=city, values=price)"  )
# Display the plot
g.figure.show()
read = input("Wait for me....5")