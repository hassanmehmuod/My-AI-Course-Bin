import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

data = pd.DataFrame({'x': np.arange(100), 'y': np.random.rand(100).cumsum()})

sns.set_theme(style='darkgrid')
sns.lineplot(x='x', y='y', data=data)
plt.show()

df = pd.read_csv('StartupUSA-DataSet/startup_growth_investment_data.csv', delimiter=",")
dffilter = df.head(40)

sns.set(style="whitegrid")

g = sns.displot(data=dffilter, x="Industry", y="Investment Amount (USD)", hue="Country", kind='hist')
g.figure.suptitle("Startup Displot Hist")
g.figure.show()
read = input("Wait for me....")

g = sns.scatterplot(x='Industry', y='Investment Amount (USD)', data=dffilter)
g.figure.suptitle("Startup Scatter")
g.figure.show()
read = input("Wait for me....")

g = sns.barplot(data=dffilter, x="Industry", y="Investment Amount (USD)", legend=False)
g.figure.suptitle("Startup Bar")
g.figure.show()
read = input("Wait for me....")