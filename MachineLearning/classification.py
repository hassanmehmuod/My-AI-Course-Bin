import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
from sklearn.model_selection import train_test_split

test_df = pd.read_csv("MachineLearning/test.csv")
train_df = pd.read_csv("MachineLearning/train.csv")
print(test_df.head())

train_df.plot.scatter(x='ram', y='price_range', title='Scatter Plot of ram and price range');
plt.show()

X_train = train_df.drop(columns=['price_range'])
y_train = train_df['price_range']

SEED = 200
X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size = 0.2, random_state=SEED)

print(X_train.shape)
print(X_test.shape)

from sklearn.linear_model import LogisticRegression

regressor = LogisticRegression()
regressor.fit(X_train, y_train)

