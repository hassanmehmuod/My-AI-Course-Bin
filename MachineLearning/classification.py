import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
from sklearn.model_selection import train_test_split

test_df = pd.read_csv("MachineLearning/test.csv")
train_df = pd.read_csv("MachineLearning/train.csv")
print(test_df.head())

print(train_df.info())
print(train_df.describe())


print("Missing values:\n", train_df.isnull().sum())
print(train_df.corr()['price_range'].sort_values(ascending=False))

train_df.plot.scatter(x='ram', y='price_range', title='Scatter Plot of ram and price range');
plt.show()

X_train = train_df.drop(columns=['price_range'])
y_train = train_df['price_range']

SEED = 200
X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size = 0.2, random_state=SEED)

print(X_train.shape)
print(X_test.shape)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=2005)
model.fit(X_train_scaled, y_train)

print("Training done")

y_pred = model.predict(X_test_scaled)
print(y_pred)

from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)
print(accuracy)
from sklearn.metrics import classification_report, confusion_matrix, f1_score
import seaborn as sns

print("F1 Score (macro):", f1_score(y_test, y_pred, average='macro'))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6,5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix - Logistic Regression')
plt.show()